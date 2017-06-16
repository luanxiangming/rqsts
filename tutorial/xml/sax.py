import xml.sax

"""python使用SAX解析xml
SAX是一种基于事件驱动的API。
利用SAX解析XML文档牵涉到两个部分:解析器和事件处理器。
解析器负责读取XML文档,并向事件处理器发送事件,如元素开始跟元素结束事件;
而事件处理器则负责对事件作出相应,对传递的XML数据进行处理。
1、对大型文件进行处理；
2、只需要文件的部分内容，或者只需从文件中得到特定信息。
3、想建立自己的对象模型的时候。
在python中使用sax方式处理xml要先引入xml.sax中的parse函数，还有xml.sax.handler中的ContentHandler。
"""


class MovieHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.CurrentData = ""
		self.type = ""
		self.format = ""
		self.year = ""
		self.rating = ""
		self.stars = ""
		self.description = ""

	'''元素开始调用
	遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典'''

	def startElement(self, name, attrs):
		self.CurrentData = name
		if name == 'movie':
			print('*****Movie*****')
			title = attrs['title']
			print('Title: ' + title)

	'''元素结束调用
	遇到XML结束标签时调用'''

	def endElement(self, name):
		if self.CurrentData == 'type':
			print('Type: ' + self.type)
		elif self.CurrentData == 'format':
			print('Format: ' + self.format)
		elif self.CurrentData == 'year':
			print('Year: ' + self.year)
		elif self.CurrentData == 'stars':
			print('Stars: ' + self.stars)
		elif self.CurrentData == 'description':
			print('Description: ' + self.description)
		self.CurrentData = ''

	'''读取字符, 调用时机：
	从行开始，遇到标签之前，存在字符，content的值为这些字符串。
	从一个标签，遇到下一个标签之前， 存在字符，content的值为这些字符串。
	从一个标签，遇到行结束符之前，存在字符，content的值为这些字符串。
	标签可以是开始标签，也可以是结束标签。
	'''

	def characters(self, content):
		if self.CurrentData == 'type':
			self.type = content
		elif self.CurrentData == 'format':
			self.format = content
		elif self.CurrentData == 'year':
			self.year = content
		elif self.CurrentData == 'stars':
			self.stars = content
		elif self.CurrentData == 'description':
			self.description = content


if __name__ == '__main__':
	# 创建一个新的解析器对象并返回
	parser = xml.sax.make_parser()
	# turn off namepsaces
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)

	handler = MovieHandler()
	parser.setContentHandler(handler)

	parser.parse('movies.xml')
