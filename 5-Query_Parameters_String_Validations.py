# @Time: 2022/3/28 16:56
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:5-Query_Parameters_String_Validations.py

from typing import Optional, List
from fastapi import FastAPI, Query


app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
We are going to enforce that even though q is optional, 
whenever it is provided, its length doesn't 
exceed 50 characters.
'''

@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
Have in mind that the most important part to make a parameter 
optional is the part: = None

or the: = Query(None)
'''


#add more validations
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


#You can define a regular expression that the parameter should match
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
'''
^: starts with the following characters, doesn't have characters before.
fixedquery: has the exact value fixedquery.
$: ends there, doesn't have any more characters after fixedquery.
'''

#default value besides None
@app.get("/items/")
async def read_items(q: str = Query("fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# $$$$$ make it required
#not required: q: str  or  q: Optional[str] = None
#or q: Optional[str] = Query(None, min_length=3)

'''
So, when you need to declare a value as required while using Query, 
you can use ... as the first argument:
'''
@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
If you hadn't seen that ... before: it is a special single value, 
it is part of Python and is called "Ellipsis".
'''

#Query parameter list / multiple values
@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items

# Query parameter list / multiple values

# Query parameter list / multiple values with defaults

@app.get("/items/")
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items

# You can also use list directly instead of List[str] (or list[str] in Python 3.9+)

# @app.get("/items/")
# async def read_items(q: list = Query([])):
#     query_items = {"q": q}
#     return query_items


# Declare more metadata
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Alias parameters
# Imagine that you want the parameter to be item-query.
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results



'''
Deprecating parameters¶
Now let's say you don't like this parameter anymore.

You have to leave it there a while because there are clients 
using it, but you want the docs to clearly show it as deprecated.

'''
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Exclude from OpenAPI
@app.get("/items/")
async def read_items(
    hidden_query: Optional[str] = Query(None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}


"""
Generic validation and metadata:
    alias
    titie
    description
    deprecated
    
Validations specific for strings:
    min_length
    max_length
    regex
"""
