# @Time: 2022/3/30 17:01
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:12-Cookie_Parameters.py

# You can define Cookie parameters the same way
# you define Query and Path parameters.


from typing import Optional

from fastapi import Cookie, FastAPI

app = FastAPI()

#ou can pass all the extra validation or annotation parameters
@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}