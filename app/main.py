import logging
import uuid

from api.v1 import v1_api_router
from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI

app = FastAPI()


def set_routers(_app: FastAPI) -> None:
    """
    This is the main entry point for the FAST API application.
    """
    # v1 api
    _app.include_router(
        v1_api_router,
        prefix='/v1',
    )


def set_middleware(_app: FastAPI):
    # set request id middleware
    _app.add_middleware(
        CorrelationIdMiddleware, header_name='request_id',
        generator=lambda: str(uuid.uuid4())[:8], validator=None, transformer=lambda a: a,
    )


logging.critical('=================== Process start ===================')
app = FastAPI()
# middleware
set_middleware(app)
# router
set_routers(app)


@app.on_event('startup')
async def startup_event():
    logging.info('=================== Application start ===================')


@app.on_event('shutdown')
def shutdown_event():
    logging.critical('=================== Application shutdown ===================')
