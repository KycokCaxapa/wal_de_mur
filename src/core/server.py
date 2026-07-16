from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from src.server.devices.led.ota import router as ota_router
from src.server.endpoints import router


app = FastAPI()

app.include_router(ota_router)
app.include_router(router)

origins = []

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_methods=['POST', 'GET', 'PUT', 'DELETE'],
                   allow_headers=['*'])
