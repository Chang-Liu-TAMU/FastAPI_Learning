# @Time: 2022/4/14 18:24
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:27-CORS.py

# CORS (Cross-Origin Resource Sharing)

'''
CORS or "Cross-Origin Resource Sharing"
refers to the situations when a frontend running in a browser has JavaScript code
that communicates with a backend, and the backend is in a different "origin" than
the frontend.
'''

'''
Origin¶
An origin is the combination of protocol (http, https), domain (myapp.com, localhost, localhost.tiangolo.com), and port (80, 443, 8080).

So, all these are different origins:

http://localhost
https://localhost
http://localhost:8080
Even if they are all in localhost, they use different protocols or ports, so, they are different "origins"
'''


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


'''
The default parameters used by the CORSMiddleware implementation are restrictive by default, 
so you'll need to explicitly enable particular origins, methods, or headers, in order for 
browsers to be permitted to use them in a Cross-Domain context.
'''

'''
The middleware responds to two particular types of HTTP request...

CORS preflight requests¶
These are any OPTIONS request with Origin and Access-Control-Request-Method headers.

In this case the middleware will intercept the incoming request and respond with appropriate CORS headers, 
and either a 200 or 400 response for informational purposes.

Simple requests¶
Any request with an Origin header. In this case the middleware will pass the request through as normal, 
but will include appropriate CORS headers on the response.
'''