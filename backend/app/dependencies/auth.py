from fastapi import Header, HTTPException, status
from firebase_admin import auth

def get_current_user(authorization: str = Header(None)):
    """Kiểm tra Token từ Frontend gửi lên"""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bạn chưa đăng nhập hoặc Token không hợp lệ",
        )
    
    # Lấy token sau chữ 'Bearer '
    token = authorization.split(" ")[1]
    
    try:
        # Xác thực token với Firebase
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Phiên đăng nhập hết hạn, vui lòng đăng nhập lại",
        )