# @Time: 2022/3/31 10:58
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:19-Request-Forms-and-Files.py

'''
*data -- (optional) Dictionary or list of tuples [(key, value)]
(will be form-encoded), bytes, or file-like object to send in
the body of the Request.

*files -- (optional) Dictionary of 'name': file-like-objects (or {'name': file-tuple})
for multipart encoding upload. file-tuple can be a 2-tuple ('filename', fileobj),
3-tuple ('filename', fileobj, 'content_type') or a 4-tuple ('filename', fileobj, 'content_type', custom_headers),
 where 'content-type' is a string defining the content type of the given file and custom_headers a dict-like object
 containing additional headers to add for the file.


I  guess the data will be encoded as content-type application/x-www-form-urlencoded in the http-request,
whereas files will be encoded as multipart/form-data. The latter also holds if you pass both data and files.
This can also be seen by viewing the resulting request.headers and request.body.

'''

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(
    file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }



