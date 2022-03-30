# @Time: 2022/3/28 15:40
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:1-First_Steps.py

"""
POST   -->  OPTIONS
GET    -->  HEAD
PUT    -->  PATCH
DELETE -->  TRACE
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}

#uvicorn main:app --reload
#interactive API docs: 0.0.0.0/docs
#alternative API docs: 0.0.0.0/redocs
#check OpenAPI schemas: 0.0.0.0/openapi.json

