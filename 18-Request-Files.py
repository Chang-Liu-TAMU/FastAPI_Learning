# @Time: 2022/3/31 9:52
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:18-Request-Files.py

'''
You can define files to be uploaded by the client using File

info:
    To receive uploaded files, first install python-multipart.

    E.g. pip install python-multipart.

    This is because uploaded files are sent as "form data".
'''

# body -> form -> file
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    #Using UploadFile has several advantages over bytes
    return {"filename": file.filename}

'''
UploadFile has the following async methods:
    write(data)
    read(size)
    seek(offset)
        --await myfile.seek(0)
    close()
    
    all these methods are async method. you need to "await" them
    like:
        contents = await myfile.read()
'''
#When you use the async methods, FastAPI runs the file methods
# in a threadpool and awaits for them.


#  ********* what is "Form Data"  ************

'''
The way HTML forms (<form></form>) sends the data to the server 
normally uses a "special" encoding for that data, it's different 
from JSON.
'''


# Optional File Upload
from typing import Optional
@app.post("/files/")
async def create_file(file: Optional[bytes] = File(None)):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: Optional[UploadFile] = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}


# UploadFile with Additional Metadata
@app.post("/files/")
async def create_file(file: bytes = File(..., description="A file read as bytes")):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile = File(..., description="A file read as UploadFile")
):
    return {"filename": file.filename}


# Multiple File Uploads
from typing import List
from fastapi.responses import HTMLResponse
@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


# Multiple File Uploads with Additional Metadata
@app.post("/uploadfiles/")
async def create_upload_files(
    files: List[UploadFile] = File(..., description="Multiple files as UploadFile")
):
    return {"filenames": [file.filename for file in files]}

