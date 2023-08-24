import uvicorn
from fastapi import FastAPI

from src.backend.api.v1 import root_router, user_router, folder_router, place_router, tag_router

app = FastAPI()

app.include_router(root_router)
app.include_router(user_router)
app.include_router(folder_router)
app.include_router(place_router)
app.include_router(tag_router)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
