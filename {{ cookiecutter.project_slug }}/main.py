import logging
import sys

import sentry_sdk
from aiohttp import web
from aiohttp_swagger import setup_swagger
from routes import routespatters
from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from settings import SENTRY_DSN, config
from webaio.middlewares import api_exception_handler


sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[AioHttpIntegration()]
)


def create_web_app():
    app = web.Application(middlewares=[api_exception_handler])
    # Add routes to app
    app['config'] = config
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
