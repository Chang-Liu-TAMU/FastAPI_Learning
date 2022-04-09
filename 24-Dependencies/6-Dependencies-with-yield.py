# @Time: 2022/4/7 9:33
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:6-Dependencies-with-yield.py

# Dependencies with yield
# FastAPI supports dependencies that do some extra steps after finishing.
# To do this, use yield instead of return, and write the extra steps after.

# Any function that is valid to use with:
#
# @contextlib.contextmanager or
# @contextlib.asynccontextmanager
# would be valid to use as a FastAPI dependency.
#
# In fact, FastAPI uses those two decorators internally.

class DBSession:
    def close(self):
        pass


async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()


def generate_dep_a():
    pass

def generate_dep_b():
    pass

def generate_dep_c():
    pass

from fastapi import Depends


async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()


async def dependency_b(dep_a=Depends(dependency_a)):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)


async def dependency_c(dep_b=Depends(dependency_b)):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)

#note
# You can still raise exceptions including HTTPException before the yield. But not after.

class MySuperContextManager:
    def __init__(self):
        self.db = DBSession()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


async def get_db():
    with MySuperContextManager() as db:
        yield db


