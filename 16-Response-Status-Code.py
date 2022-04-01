# @Time: 2022/3/31 9:35
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:16-Response-Status-Code.py

from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

# status_code can alternatively also receive an
# IntEnum, such as Python's http.HTTPStatus.

'''
About HTTP status codes

100 and above are for "Information"

200 and above are for "Successful" responses.

300 and above are for "Redirection"

400 and above are for "Client error" responses

500 and above are for server errors.
'''


# Shortcut to remember the names
from fastapi import status


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}