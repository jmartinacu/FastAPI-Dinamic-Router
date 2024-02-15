from fastapi import FastAPI
from utils.dynamic_router import Routers
from modules.core.core import router_urls as core_urls

URLS_ENDPOINTS = core_urls

APP_PREFIX = '/v1/api/'

app = FastAPI()

Routers(
    app=app,
    absolute_routes=URLS_ENDPOINTS,
    prefix=APP_PREFIX
)()


@app.get('/')
def root():
    return 'Hello world!'


@app.get(APP_PREFIX)
def root():
    return 'Hello fastAPI app!'
