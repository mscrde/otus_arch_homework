from aiohttp import web


def init_app():
    app = web.Application()
    app.add_routes([
        web.get('/health/', handle_health),
        web.get('/health', handle_health),
    ])
    web.run_app(app, port=8000)


async def handle_health(request):
    return web.json_response({"status": "OK"})

if __name__ == '__main__':
    init_app()
