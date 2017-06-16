import unittest, os, sys, stat


class PythonOS(unittest.TestCase):
	def setUp(self):
		self.origin = os.getcwd()

	def tearDown(self):
		os.chdir(self.origin)

	def test_access(self):
		# 检验权限模式 os.access(path, mode)
		self.assertTrue(os.access('tmp/foo.txt', os.F_OK))  # os.F_OK: 作为access()的mode参数，测试path是否存在
		self.assertTrue(os.access('tmp/foo.txt', os.R_OK))  # os.R_OK: 包含在access()的mode参数中， 测试path是否可读
		self.assertTrue(os.access('tmp/foo.txt', os.W_OK))  # os.W_OK 包含在access()的mode参数中 ， 测试path是否可写
		self.assertTrue(os.access('tmp/foo.txt', os.X_OK))  # os.X_OK 包含在access()的mode参数中 ，测试path是否可执行

	def test_chdir(self):
		# 改变当前工作目录改变当前工作目录 os.chdir(path)
		print("当前目录: " + os.getcwd())
		os.chdir('tmp')
		print("改变目录: " + os.getcwd())
		os.chdir('/Users')
		print("改变目录: " + os.getcwd())

	def test_chflags(self):
		"""flags：
		stat.UF_NODUMP: 非转储文件
		stat.UF_IMMUTABLE: 文件是只读的
		stat.UF_APPEND: 文件只能追加内容
		stat.UF_NOUNLINK: 文件不可删除
		stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
		stat.SF_ARCHIVED: 可存档文件(超级用户可设)
		stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
		stat.SF_APPEND: 文件只能追加内容(超级用户可设)
		stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
		stat.SF_SNAPSHOT: 快照文件(超级用户可设)
		"""
		flags = stat.UF_NOUNLINK  # 为文件设置标记，使得它不能被删除
		retval = os.chflags('tmp/foo.txt', flags)
		self.assertIsNone(retval)

	def test_chmod(self):
		"""
		stat.S_IXOTH: 其他用户有执行权0o001
		stat.S_IWOTH: 其他用户有写权限0o002
		stat.S_IROTH: 其他用户有读权限0o004
		stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
		stat.S_IXGRP: 组用户有执行权限0o010
		stat.S_IWGRP: 组用户有写权限0o020
		stat.S_IRGRP: 组用户有读权限0o040
		stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
		stat.S_IXUSR: 拥有者具有执行权限0o100
		stat.S_IWUSR: 拥有者具有写权限0o200
		stat.S_IRUSR: 拥有者具有读权限0o400
		stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
		stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
		stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
		stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
		stat.S_IREAD: windows下设为只读
		stat.S_IWRITE: windows下取消只读
		"""
		self.assertIsNone(os.chmod('tmp/foo.txt', stat.S_IRWXU))

	def test_chown(self):
		# 更改文件所有者 os.chown(path, uid, gid)
		pass

	def test_chroot(self):
		# 更改当前进程的根目录为指定的目录，使用该函数需要管理员权限 os.chroot(path)
		pass

	def test_closerange(self):
		# 关闭所有文件描述符 fd，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略 os.closerange(fd_low, fd_high)
		pass


if __name__ == '__main__':
	unittest.main()
