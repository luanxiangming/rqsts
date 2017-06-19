import asyncio
import aiohttp
from aiohttp import web

"""
asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。

"""


async def index(request):
	await asyncio.sleep(1)
	return web.Response(body=b'<h1>index</h1>', content_type='text/html')


async def hello(request):
	await asyncio.sleep(1)
	text = '<h3>Hello, %s</h3>' % request.match_info['name']
	return web.Response(body=text.encode('UTF-8'), content_type='text/html')


# aiohttp的初始化函数init()也是一个coroutine
async def init(loop):
	print('module aiohttp:')
	print(dir(aiohttp))

	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	app.router.add_route('GET', '/{name}', hello)

	# loop.create_server()利用asyncio创建TCP服务
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
	print('Server started at http://127.0.0.1:8000...')
	return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
