# @Time: 2022/3/29 14:20
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:9-Body-Nested-Models.py

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list = [] # List fields


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results



# List fields with type parameter
from typing import List, Optional
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = [] #list[str] for python >= 3.9


from typing import Optional, Set
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()



# Nested Models
class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []
    image: Optional[Image] = None

    # {
    #     "name": "Foo",
    #     "description": "The pretender",
    #     "price": 42.0,
    #     "tax": 3.2,
    #     "tags": ["rock", "metal", "bar"],
    #     "image": {
    #         "url": "http://example.com/baz.jpg",
    #         "name": "The Foo live"
    #     }
    # }


from pydantic import BaseModel, HttpUrl
# Special types and validation
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[Image] = None


# Attributes with lists of submodels
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None


# Deeply nested models
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]


# Bodies of pure lists
class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images


# Bodies of arbitrary dicts
from typing import Dict
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights