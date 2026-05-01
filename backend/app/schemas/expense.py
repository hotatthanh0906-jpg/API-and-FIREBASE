from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Cấu trúc khi người dùng gửi dữ liệu lên
class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str

# Cấu trúc khi Backend trả dữ liệu về cho Frontend
class ExpenseResponse(ExpenseCreate):
    id: str
    timestamp: datetime

    class Config:
        from_attributes = True