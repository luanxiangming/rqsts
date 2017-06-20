from aiohttp import web
import asyncio
import logging


host = '127.0.0.1'
port = 9000


async def index(request):
	return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)

	srv = await loop.create_server(app.make_handler(), host, port)
	logging.info("Server get started at %s: %d..." % (host, port))
	return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
