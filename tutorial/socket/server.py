import socket

print('module socket: ')
print(dir(socket))

# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
port = 9999

# 绑定端口
server_socket.bind((host, port))

# 设置最大连接数，超过后排队
server_socket.listen(5)

while True:
	# 建立客户端连接
	client_socket, addr = server_socket.accept()
	print('连接地址: ' + str(addr))

	msg = '欢迎访问\n'
	client_socket.send(msg.encode('utf-8'))
	client_socket.close()
