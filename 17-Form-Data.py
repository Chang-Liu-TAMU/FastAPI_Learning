# @Time: 2022/3/31 9:44
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:17-Form-Data.py

#When you need to receive form fields instead of JSON, you can use Form.

'''
To use forms, first install python-multipart.

E.g. pip install python-multipart.
'''


from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}

"""
info:

Form is a class that inherits directly from Body.

"""

"""
tip:

To declare form bodies, you need to use Form explicitly, 
because without it the parameters would be interpreted as query 
parameters or body (JSON) parameters.
"""



'''
Data from forms is normally encoded using the "media type" 
application/x-www-form-urlencoded.


But when the form includes files, it is encoded as multipart/form-data. 
You'll read about handling files in the next chapter.
'''
