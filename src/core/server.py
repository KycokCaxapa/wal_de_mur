from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from src.server.server import router


app = FastAPI()
origins = []

app.include_router(router)

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_methods=['POST', 'GET', 'PUT', 'DELETE'],
                   allow_headers=['*'])
