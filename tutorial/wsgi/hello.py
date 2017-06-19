"""
实现Web应用程序的WSGI处理函数
无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。
HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。
"""


def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])  # response header
	body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:])
	print('发起请求的所有信息：')
	for k, v in environ.items():
		print(k, v)
	return [body.encode('UTF-8')]  # response body
