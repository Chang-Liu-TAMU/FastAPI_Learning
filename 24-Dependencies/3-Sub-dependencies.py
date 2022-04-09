# @Time: 2022/4/7 8:55
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3-Sub-dependencies.py


# Sub-dependencies
# You can create dependencies that have sub-dependencies.
#
# They can be as deep as you need them to be.
#
# FastAPI will take care of solving them.

from typing import Optional

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: Optional[str] = None):
    return q


def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: Optional[str] = Cookie(None)
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}



