# @Time: 2022/5/21 19:58
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:main.py


from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    pass
    # uvicorn app.main: app - -reload
    # And open the docs at http://127.0.0.1:8000/docs
