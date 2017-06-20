import aiomysql
import asyncio
import logging
from orm import Model, StringField, IntegerField

logging.basicConfig(level=logging.INFO)

"""创建连接池
我们需要创建一个全局的连接池，每个HTTP请求都可以从连接池中直接获取数据库连接。
连接池由全局变量__pool存储，缺省情况下将编码设置为utf8，自动提交事务：
"""


def log(sql, args=()):
	logging.info('SQL: %s' % sql)


async def create_pool(loop, **kw):
	logging.info("Creating database connection pool...")
	global __pool
	__pool = await aiomysql.create_pool(
		host=kw.get('host', 'localhost'),
		port=kw.get('port', '3306'),
		user=kw['user'],
		password=kw['password'],
		db=kw['db'],
		charset=kw.get('charset', 'utf8'),
		autocommit=kw.get('autocommit', True),
		maxsize=kw.get('maxsize', 10),
		minsize=kw.get('minsize', 1),
		loop=loop
	)


""" 要执行SELECT语句，我们用select函数执行，需要传入SQL语句和SQL参数 """


async def select(sql, args, size=0):
	log(sql, args)
	global __pool
	with (await __pool) as conn:
		# await将调用一个子协程（也就是在一个协程中调用另一个协程）并直接获得子协程的返回结果
		cur = await conn.cursor(aiomysql.DictCursor)
		'''SQL语句的占位符是?，而MySQL的占位符是%s，select()函数在内部自动替换。
		注意要始终坚持使用带参数的SQL，而不是自己拼接SQL字符串，这样可以防止SQL注入攻击。
		'''
		await cur.execute(sql.replace('?', '%s'), args or ())
		if size:
			rs = await cur.fetchmany(size)
		else:
			rs = await cur.fetchall()
		await cur.close()
		logging.info('row returned: %d' % len(rs))
		return rs


""" 执行INSERT、UPDATE、DELETE语句. 这3种SQL的执行都需要相同的参数，以及返回一个整数表示影响的行数 """


async def execute(sql, args):
	log(sql)
	with (await __pool) as conn:
		try:
			cur = await conn.cursor()
			await cur.execute(sql.replace('?', '%s'), args)
			affected = cur.rowcount
			await cur.close()
		except BaseException:
			raise
		return affected


class User(Model):
	__table__ = 'users'
	# 类级别上定义的属性用来描述User对象和表的映射关系，而实例属性必须通过__init__()方法去初始化
	id = IntegerField(primary_key=True)
	name = StringField()


class Model(dict, metaclass=ModelMetaclass):
	""" 所有ORM映射的基类Model
	Model从dict继承，所以具备所有dict的功能，同时又实现了特殊方法__getattr__()和__setattr__()，因此又可以像引用普通字段那样写：
	user['id']
	123
	user.id
	123
	"""

	def __init__(self):
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"Model's object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def getValue(self, key):
		return getattr(self, key, None)

	def getValueOrDefault(self):
		value = getattr(self, key, None)
		if value is None:
			field = self.__mappings__[key]
			if field.default is not None:
				value = field.default() if callable(field.default) else field.default
				logging.debug('use default value for %s: %s' % (key, str(value)))
				setattr(self, key, value)
		return value

	""" 让所有子类调用class方法, User类现在就可以通过类方法实现主键查找：
	user = await User.find('123') 
	"""
	@classmethod
	async def find(cls, pk):
		rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
		if len(rs) == 0:
			return None
		return cls(**rs[0])

	""" 实例方法，可以让所有子类调用实例方法, 这样就可以把一个User实例存入数据库：
	user = User(id=123, name='Michael')
	await user.save()
	
	特别注意：user.save()没有任何效果，因为调用save()仅仅是创建了一个协程，并没有执行它。
	一定要用：await user.save()才真正执行了INSERT操作。
	"""
	async def save(self):
		args = list(map(self.getValueOrDefault(), self.__fields__))
		args.append(self.getValueOrDefault(self.__primary_key__))
		rows = await execute(self.__insert__, args)
		if rows != 1:
			logging.warning('Failed to insert rows: %s' % rows)


class Field(object):
	""" Field和各种Field子类 """
	def __init__(self, name, column_type, primary_key, default):
		self.name = name
		self.column_type = column_type
		self.primary_key = primary_key
		self.default = default

	def __str__(self):
		return '<%s, %s: %s>' % (self.__class__.__name__, self.column_type, self.name)


class StringField(Field):
	def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
		super.__init__(name, primary_key, default, ddl)


class ModelMetaclass(type):
	""" Model只是一个基类, 通过metaclass：ModelMetaclass将具体的子类如User的映射信息读取出来.
	这样，任何继承自Model的类（比如User），会自动通过ModelMetaclass扫描映射关系，并存储到自身的类属性如__table__、__mappings__中。
	"""
	def __new__(cls, name, bases, attrs):
		# 排除Model类本身
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)

		# 获取table名称
		table_name = attrs.get('__table__', None) or name
		logging.info('Found model: %s(table: %s)' % (name, table_name))

		mappings = dict()
		fields = []
		primaryKey = None
		for k, v in attrs.items():
			if isinstance(v, Field):
				logging.info('Found mapping: %s==>%s' % (k, v))
				mappings[k] = v
				if v.primary_key:
					# 找到主键:
					if primaryKey:
						raise RuntimeError('duplicate primary key for field: %s' % k)
					primaryKey = k
				else:
					fields.append(k)
		if not primaryKey:
			raise RuntimeError('primary key not found')
		for k in mappings.keys():
			attrs.pop(k)
		escaped_fields = list(map(lambda f: '`%s`' % f, fields))
		attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
		attrs['__table__'] = tableName
		attrs['__primary_key__'] = primaryKey  # 主键属性名
		attrs['__fields__'] = fields  # 除主键外的属性名

		# 构造默认的SELECT, INSERT, UPDATE和DELETE语句
		attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
		attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (
		tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
		attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (
		tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
		attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
		return type.__new__(cls, name, bases, attrs)

