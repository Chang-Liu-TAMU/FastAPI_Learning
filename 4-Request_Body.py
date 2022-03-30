# @Time: 2022/3/28 16:41
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:4-Request_Body.py

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

#note: when a model attribute has a default value,
# it is not required. Otherwise, it is required
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

'''
FastAPI will recognize that the function parameters that match path parameters 
should be taken from the path, and that function parameters that are declared
 to be Pydantic models should be taken from the request body.
'''

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


'''
The function parameters will be recognized as follows:

If the parameter is also declared in the path, it will be used as a path parameter.
If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.
'''

