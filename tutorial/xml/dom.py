from xml.dom.minidom import parse

'''
文件对象模型（Document Object Model，简称DOM），是W3C组织推荐的处理可扩展置标语言的标准编程接口。
一个 DOM 的解析器在解析一个 XML 文档时，一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里，
之后你可以利用DOM 提供的不同的函数来读取或修改文档的内容和结构，也可以把修改过的内容写入xml文件。
python中用xml.dom.minidom来解析xml文件，实例如下
'''

# 使用minidom解析器打开 XML 文档
DOMTree = parse('movies.xml')
collection = DOMTree.documentElement
if collection.hasAttribute('shelf'):
	print('Root element: {}'.format(collection.getAttribute('shelf')))

# 在集合中获取所有电影
movies = collection.getElementsByTagName('movie')

for movie in movies:
	print('*****Movie*****')
	if movie.hasAttribute('title'):
		print('Title: {}'.format(movie.getAttribute('title')))
	type = movie.getElementsByTagName('type')[0]
	print('Type: {}'.format(type.childNodes[0].data))

	format = movie.getElementsByTagName('format')[0]
	print('Format: {}'.format(format.childNodes[0].data))

	if movie.getElementsByTagName('year'):
		year = movie.getElementsByTagName('year')[0]
		print('Year: {}'.format(year.childNodes[0].data))

	rating = movie.getElementsByTagName('rating')[0]
	print('Rating: {}'.format(rating.childNodes[0].data))

	stars = movie.getElementsByTagName('stars')[0]
	print('Stars: {}'.format(stars.childNodes[0].data))

	description = movie.getElementsByTagName('description')[0]
	print('Description: {}'.format(description.childNodes[0].data))