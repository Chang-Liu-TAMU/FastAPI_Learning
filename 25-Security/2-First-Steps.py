# @Time: 2022/4/8 15:54
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:2-First-Steps.py

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
