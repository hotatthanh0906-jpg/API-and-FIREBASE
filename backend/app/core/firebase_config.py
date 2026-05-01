import firebase_admin
from firebase_admin import credentials, firestore
import os

# Lấy đường dẫn tuyệt đối đến thư mục chứa file hiện tại (thư mục core)
current_dir = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(current_dir, "serviceAccountKey.json")

if not firebase_admin._apps:
    try:
        # Kiểm tra xem file có thực sự tồn tại trước khi nạp
        if os.path.exists(cred_path):
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
            print("✅ Kết nối Firebase thành công!")
        else:
            print(f"❌ KHÔNG TÌM THẤY FILE TẠI: {cred_path}")
    except Exception as e:
        print(f"❌ Lỗi khởi tạo Firebase: {e}")

def get_firestore():
    return firestore.client()