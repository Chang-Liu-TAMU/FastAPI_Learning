# @Time: 2022/3/30 17:20
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:13-Header-Parameters.py

from typing import Optional

from fastapi import FastAPI, Header
from typing import List

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}


# Automatic conversion
@app.get("/items/")
async def read_items(
    strange_header: Optional[str] = Header(None, convert_underscores=False)
):
    return {"strange_header": strange_header}


# Duplicate headers
@app.get("/items/")
async def read_items(x_token: Optional[List[str]] = Header(None)):
    return {"X-Token values": x_token}

