import logging
import sys

from aiohttp import web
from aiohttp_swagger import setup_swagger
from routes import routespatters
from webaio.middlewares import api_exception_handler


def create_web_app():
    app = web.Application(middlewares=[api_exception_handler])
    # Add routes to app
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M',
        stream=sys.stdout
    )
    app.add_routes(routespatters)
    setup_swagger(
        app,
        title="{{ cookiecutter.project_name }}",
        swagger_url="/swagger",
        ui_version=3
    )
    return app


async def get_web_app():
    return create_web_app()

app = create_web_app()

if __name__ == '__main__':
    web.run_app(app)
