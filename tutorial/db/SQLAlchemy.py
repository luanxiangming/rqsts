from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
	""" ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换 """
	# 表的名字:
	__tablename__ = 'user'

	# 表的结构:
	id = Column(String(20), primary_key=True)
	name = Column(String(20))
	grade = Column(String(20))


# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:password@localhost:3306/test')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def session_add():
	session = DBSession()  # 创建session对象, Session对象可视为当前数据库连接
	new_user = User(id='12', name='Pete', grade='8')  # 创建新User对象
	session.add(new_user)  # 添加到session
	session.commit()  # 提交即保存到数据库
	session.close()  # 关闭session


def session_query():
	session = DBSession()
	# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
	user = session.query(User).filter(User.id == '6').one()
	print(type(user), user.id, user.name, user.grade)
	session.close()


# session_add()
session_query()
