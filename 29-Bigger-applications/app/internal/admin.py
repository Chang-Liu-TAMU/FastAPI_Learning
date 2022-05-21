# @Time: 2022/5/21 19:59
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:admin.py

from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}
