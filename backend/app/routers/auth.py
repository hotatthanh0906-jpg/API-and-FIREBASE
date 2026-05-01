from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests

router = APIRouter(prefix="/auth", tags=["auth"])

# API Key chính xác từ cấu hình của bạn
FIREBASE_WEB_API_KEY = "AIzaSyBAAGfEKGIIdk-UAYS21oyMD39UT_jiev4"

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login(data: LoginRequest):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_WEB_API_KEY}"
    payload = {"email": data.email, "password": data.password, "returnSecureToken": True}
    res = requests.post(url, json=payload)
    if res.status_code != 200:
        detail = res.json().get("error", {}).get("message", "Sai thông tin đăng nhập")
        raise HTTPException(status_code=400, detail=detail)
    return res.json()

@router.post("/register")
async def register(data: LoginRequest):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_WEB_API_KEY}"
    payload = {"email": data.email, "password": data.password, "returnSecureToken": True}
    res = requests.post(url, json=payload)
    if res.status_code != 200:
        detail = res.json().get("error", {}).get("message", "Đăng ký thất bại")
        raise HTTPException(status_code=400, detail=detail)
    return {"message": "Thành công"}