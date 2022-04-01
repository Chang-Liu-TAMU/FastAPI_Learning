# @Time: 2022/4/1 15:59
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:22-JSON-Compatible-Encoder.py

# Using the jsonable_encoder
from datetime import datetime
from typing import Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Optional[str] = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data


