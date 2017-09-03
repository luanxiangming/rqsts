from os.path import join


class FileObject:
	""" 给文件对象进行包装从而确认在删除时文件流关闭 """

	def __init__(self, filepath='~', filename='sample.txt'):
		self.file = open(join(filepath, filename), 'r+')

	def __del__(self):
		self.file.close()
		del self.file


class FunctionalList:
	""" 实现了内置类型list的功能,并丰富了一些其他方法: head, tail, init, last, drop, take """

	def __init__(self, values=None):
		if values is None:
			self.values = []
		else:
			self.values = values

	def __len__(self):
		return len(self.values)

	def __getitem__(self, key):
		return self.values[key]

	def __setitem__(self, key, value):
		self.values[key] = value

	def __delitem__(self, key):
		del self.values[key]

	def __iter__(self):
		return iter(self.values)

	def __reversed__(self):
		return FunctionalList(reversed(self.values))

	def append(self, value):
		self.values.append(value)

	def head(self):
		# 获取第一个元素
		return self.values[0]

	def tail(self):
		# 获取第一个元素之后的所有元素
		return self.values[1:]

	def init(self):
		# 获取最后一个元素之前的所有元素
		return self.values[:-1]

	def last(self):
		# 获取最后一个元素
		return self.values[-1]

	def drop(self, n):
		# 获取所有元素，除了前N个
		return self.values[n:]

	def take(self, n):
		# 获取前N个元素
		return self.values[:n]
