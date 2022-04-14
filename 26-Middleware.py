# @Time: 2022/4/14 18:23
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:26-Middleware.py

'''
You can add middleware to FastAPI applications.

A "middleware" is a function that works with every request before
it is processed by any specific path operation. And also with every
 response before returning it.
'''

'''
If you have dependencies with yield, the exit code will run after the middleware.

If there were any background tasks (documented later), they will run after all the middleware.
'''


import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

