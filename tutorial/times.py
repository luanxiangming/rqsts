import unittest, time, calendar, datetime
from datetime import date

class PythonTime(unittest.TestCase):
	"""python中时间日期格式化符号：
	%y 两位数的年份表示（00-99）
	%Y 四位数的年份表示（000-9999）
	%m 月份（01-12）
	%d 月内中的一天（0-31）
	%H 24小时制小时数（0-23）
	%I 12小时制小时数（01-12）
	%M 分钟数（00=59）
	%S 秒（00-59）
	%a 本地简化星期名称
	%A 本地完整星期名称
	%b 本地简化的月份名称
	%B 本地完整的月份名称
	%c 本地相应的日期表示和时间表示
	%j 年内的一天（001-366）
	%p 本地A.M.或P.M.的等价符
	%U 一年中的星期数（00-53）星期天为星期的开始
	%w 星期（0-6），星期天为星期的开始
	%W 一年中的星期数（00-53）星期一为星期的开始
	%x 本地相应的日期表示
	%X 本地相应的时间表示
	%Z 当前时区的名称
	%% %号本身
	"""

	''' Time 模块 '''
	def test_time(self):
		print('module time: ')
		print(dir(time))
		print('Ticks from the beginning: ' + str(time.time())) #时间间隔是以秒为单位的浮点小数
		print('LocalTime: ' + str(time.localtime())) #从返回浮点数的时间辍方式向时间元组转换
		print('ASCTime: ' + time.asctime(time.localtime())) #接受时间元组并返回一个可读的形式
		print('CTime: ' + time.ctime()) #等于asctime()
		print('GMTime: ' + str(time.gmtime())) #接收时间戳并返回格林威治天文时间下的时间元组

		''' strftime接收时间元组，并按指定格式返回以可读字符串表示的当地时间 '''
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())) #格式化成2016-03-20 11:45:39
		print(time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())) #格式化成Sat Mar 28 22:24:24 2016

		''' 将格式字符串转换为时间戳 '''
		a = "Sat Mar 28 22:24:24 2016"
		time_tuple = time.strptime(a, '%a %b %d %H:%M:%S %Y') # strptime根据指定格式把一个时间字符串解析为时间元组
		time_stamp = time.mktime(time_tuple) # mktime接受时间元组并返回时间戳
		print('mktime: ' + str(time_stamp))

		''' 以浮点数计算的秒数返回当前的CPU时间
		在第一次调用的时候，返回的是程序运行的实际时间；
		以第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔'''
		t0 = time.clock()
		time.sleep(2)
		print(time.clock() - t0)

		print('Altzone: ' + str(time.altzone)) #返回格林威治西部的夏令时地区的偏移秒数
		print('TimeZone: ' + repr(time.timezone)) # 当地时区（未启动夏令时）距离格林威治的偏移秒数
		print(('TZName: ' + repr(time.tzname))) # 包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的

	''' 日历（Calendar）模块 '''
	def test_calendar(self):
		print('module calendar: ')
		print(dir(calendar))

		'''calendar.calendar(year,w=2,l=1,c=6)返回一个多行字符串格式的year年年历，
		3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数'''
		print(calendar.calendar(1983, 2, 1, 6))

		'''calendar.month(year, month, w=2, l=1)
		返回一个多行字符串格式的year年month月日历，两行标题，一周一行。
		每日宽度间隔为w字符。每行的长度为7 * w + 6。l是每星期的行数。'''
		print(calendar.month(2017, 6, 2, 1))
		print(calendar.month(2017, 7))

		print("1st weekday: " + repr(calendar.firstweekday())) # 返回当前每周起始日期的设置
		self.assertFalse(calendar.isleap(2017))
		self.assertEqual(calendar.leapdays(2010, 2017), 2) #返回在Y1，Y2两年之间的闰年总数。

		''' 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;
		范围内的日子都由该月第几日表示，从1开始。'''
		print('Weeks in Month: ' + str(calendar.monthcalendar(2017, 6)))

		'''计算每个月天数
		第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数。
		以下实例输出的意思为 1983 年 7 月份的第一天是星期五，该月总共有 31 天'''
		self.assertEqual(calendar.monthrange(1983, 7), (4, 31))

		# 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳
		print(calendar.timegm(time.localtime()))

		# 返回给定日期的日期码。0（星期一）到6（星期日）。月份为1（一月） 到12（12月）。
		self.assertEqual(calendar.weekday(2017, 6, 15), 3)


	''' 获取昨天日期 '''
	def test_datetime(self):
		print('module datetime: ')
		print(dir(datetime))
		today = datetime.date.today()
		print('Today: ' + str(today))

		one_day = datetime.timedelta(days=1)
		print('Yesterday: ' + str(today - one_day))

	def test_date(self):
		print('module date: ')
		print(dir(date))
		print("Today: " + str(date.today()))
		print(date.today().strftime('%d-%m-%y. %d %b %Y is a %a on the %dth day of %B'))

		birthday = date(1983, 7, 14)
		print(date.today() - birthday) # dates support calendar arithmetic

if __name__ == '__main__':
	unittest.main()