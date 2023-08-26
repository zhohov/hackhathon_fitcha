import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from src.backend.api.v1 import root_router, user_router, folder_router, place_router, tag_router, city_router

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(root_router)
app.include_router(user_router)
app.include_router(folder_router)
app.include_router(place_router)
app.include_router(tag_router)
app.include_router(city_router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
