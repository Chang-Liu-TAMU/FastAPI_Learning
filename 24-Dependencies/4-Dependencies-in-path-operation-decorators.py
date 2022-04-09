# @Time: 2022/4/7 9:08
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:4-Dependencies-in-path-operation-decorators.py

# Dependencies in path operation decorators
# For those cases, instead of declaring a path operation function parameter
# with Depends, you can add a list of dependencies to the path operation decorator.

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
