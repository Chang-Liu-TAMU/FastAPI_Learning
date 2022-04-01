# @Time: 2022/4/1 17:03
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:1-First-Steps.py

from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

# You can think of it as a path operation function without the "decorator"
# (without the @app.get("/some-path")).


#
# In the end, a hierarchical tree of dependencies is built, and the Dependency
# Injection system takes care of solving all these dependencies for you (and
# their sub-dependencies) and providing (injecting) the results at each step.

