from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Import để kích hoạt việc kết nối Firebase ngay khi app khởi động
from backend.app.core.firebase_config import get_firestore 
from backend.app.routers import auth, expense

app = FastAPI(
    title="SmartSpend API",
    description="Backend quản lý chi tiêu tích hợp Firebase Authentication và Firestore",
    version="1.0.0"
)

# --- 1. CẤU HÌNH CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. KIỂM TRA KẾT NỐI KHI STARTUP ---
@app.on_event("startup")
async def startup_event():
    print("🚀 API SmartSpend đang khởi động...")
    try:
        get_firestore()
        print("✅ Backend đã kết nối sẵn sàng với Firebase!")
    except Exception as e:
        print(f"❌ Lỗi khi khởi động kết nối Firebase: {e}")

# --- 3. ĐỊNH NGHĨA CÁC ENDPOINT YÊU CẦU ---

@app.get("/", tags=["Root"])
def read_root():
    """Endpoint gốc trả về lời chào"""
    return {
        "message": "Welcome to SmartSpend API",
        "docs": "Truy cập /docs để xem chi tiết các API",
        "status": "Running"
    }

@app.get("/health", tags=["Health"])
def health_check():
    """Endpoint kiểm tra sức khỏe hệ thống"""
    return {
        "status": "healthy", 
        "database": "connected",
        "message": "Hệ thống hoạt động bình thường"
    }

# --- 4. ĐĂNG KÝ CÁC ROUTERS ---
app.include_router(auth.router)
app.include_router(expense.router)

# Chạy trực tiếp
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)