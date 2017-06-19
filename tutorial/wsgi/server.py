from wsgiref.simple_server import make_server

from hello import application

"""
负责启动WSGI服务器，加载application()函数
"""

port = 8008
# 创建一个服务器，IP地址为空，端口，处理函数是application
httpd = make_server('', port, application)
print('Serving HTTP on port {}'.format(port))

# 开始监听HTTP请求:
httpd.serve_forever()

