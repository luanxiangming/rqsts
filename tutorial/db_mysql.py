import pymysql
import unittest


class PythonMySQL(unittest.TestCase):
	DB = 'spider'
	HOST = 'LOCALHOST'
	PORT = 3306
	USER = 'root'
	PASSWORD = 'password'
	CHARSET = 'utf8mb4'
	TB = 'EMPLOYEE'

	@classmethod
	def setUpClass(self):
		''' 数据库连接 '''
		self.conn = pymysql.connect(
			host=self.HOST,
			port=self.PORT,
			user=self.USER,
			password=self.PASSWORD,
			db=self.DB,
			charset=self.CHARSET,
		)
		self.cursor = self.conn.cursor()

	@classmethod
	def tearDownClass(self):
		self.conn.close()

	''' 测试数据库连接 '''

	def test_connect_database(self):
		print('module pymysql: ')
		print(dir(pymysql))

		self.cursor.execute("SELECT VERSION()")
		data = self.cursor.fetchone()
		print("MySQL Version : %s " % data)

		sql = r'SELECT * from products_taobao ORDER BY id DESC LIMIT 3'
		self.cursor.execute(sql)
		data = self.cursor.fetchall()
		print("Data : %s " % str(data))

	''' 创建数据库表 '''

	def test_create_table(self):
		sql_drop = r'DROP TABLE IF EXISTS {}'.format(self.TB)
		self.cursor.execute(sql_drop)

		sql_create = '''CREATE TABLE {}(
					FIRST_NAME CHAR(20) NOT NULL,
					LAST_NAME CHAR(20),
					AGE INT,
					SEX CHAR(1),
					INCOME FLOAT)'''.format(self.TB)
		self.cursor.execute(sql_create)

	''' 数据库插入操作 '''

	def test_insert_table(self):
		sql_insert = '''INSERT INTO {}(FIRST_NAME,
 						LAST_NAME, AGE, SEX, INCOME) 
 						VALUES ("Adam", "Smith", 1000, "M", 3000)'''.format(self.TB)
		try:
			self.cursor.execute(sql_insert)  # 执行SQL语句
			self.conn.commit()  # 向数据库提交
		except:
			self.conn.rollback()  # 发生错误时回滚

	''' 数据库查询操作 
	fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
	fetchall(): 接收全部的返回结果行.
	rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。'''

	def test_fetch_table(self):
		sql_fetch = ''' SELECT * FROM {} WHERE INCOME > 1000'''.format(self.TB)
		self.cursor.execute(sql_fetch)
		results = self.cursor.fetchall()
		for result in results:
			fname = result[0]
			lname = result[1]
			age = result[2]
			sex = result[3]
			income = result[4]
			print('firstname: {}, lastname: {}, age: {}, sex: {}, income: {}'.format(fname, lname, age, sex, income))

	''' 数据库更新操作 '''

	def test_update_table(self):
		sql_update = "UPDATE {} SET SEX='M', AGE=AGE+1".format(self.TB)
		try:
			self.cursor.execute(sql_update)
			self.conn.commit()
		except:
			self.conn.rollback()

	''' 删除操作 '''

	def test_delete_table(self):
		sql_del = "DELETE FROM {} WHERE AGE>{}".format(self.TB, 1000)
		try:
			self.cursor.execute(sql_del)
			self.conn.commit()
		except:
			self.conn.rollback()


if __name__ == '__main__':
	unittest.main()
