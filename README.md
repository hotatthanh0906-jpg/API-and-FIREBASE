## 🛠 Công nghệ sử dụng
- **Backend:** FastAPI (Python 3.9+)
- **Frontend:** Streamlit
- **Database:** Google Cloud Firestore
- **Authentication:** Firebase Auth (Identity Toolkit)

## 📌 Yêu cầu Backend (Đã đáp ứng)
Dự án hoàn thành đầy đủ các yêu cầu kỹ thuật của đề bài:
- **GET /**: Trang chào mừng và thông tin API.
- **GET /health**: Kiểm tra trạng thái kết nối hệ thống và cơ sở dữ liệu.
- **Endpoint xác thực**: Đã triển khai `/auth/login` và `/auth/register`.
- **Feature chính (POST)**: Lưu khoản chi mới vào Firestore.
- **Feature đọc dữ liệu (GET)**: Lấy danh sách chi tiêu theo từng User ID.

### . Hướng dẫn chạy Backend
Khởi động server FastAPI bằng lệnh:
Để xem các endpoint `GET /` và `GET /health` đang hoạt động như thế nào, bạn có thể kiểm tra qua 2 "cổng" chính sau đây:

### . Xem trực tiếp trên trình duyệt (Dành cho người dùng)
Khi backend của bạn đang chạy (sau khi gõ lệnh `uvicorn`), bạn hãy mở trình duyệt web (Chrome, Edge...) và truy cập vào các địa chỉ sau:

*   **Trang chào mừng (`GET /`):** 
    👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    *Kết quả mong đợi:* Bạn sẽ thấy dòng chữ `{"message": "Welcome to SmartSpend API"}`.

*   **Trang kiểm tra sức khỏe (`GET /health`):** 
    👉 [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)
    *Kết quả mong đợi:* Bạn sẽ thấy `{"status": "healthy", ...}`.

---

### . Xem qua giao diện kiểm thử (Dành cho lập trình viên)
FastAPI cung cấp một trang tài liệu tự động rất xịn sò để bạn có thể bấm "chạy thử" ngay lập tức:

*   **Link Swagger UI:** 
    👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

**Tại đây bạn có thể:**
1. Tìm đến dòng có chữ **GET /** hoặc **GET /health**.
2. Bấm vào nút **Try it out**.
3. Bấm **Execute**.
4. Xem kết quả trả về ngay tại trang đó mà không cần chuyển tab.

## 📁 Cấu trúc thư mục
```text
project-root/
├── backend/
│   ├── app/
│   │   ├── main.py          # Entry point (Endpoint /, /health và cấu hình CORS)
│   │   ├── routers/         # Điều hướng auth.py, expense.py
│   │   ├── services/        # Logic xử lý Firestore (save/load)
│   │   ├── core/            # Cấu hình Firebase Admin SDK
│   │   ├── dependencies/    # Xử lý xác thực Token
│   │   └── schemas/         # Định nghĩa kiểu dữ liệu (Pydantic models)
├── frontend/
│   └── app.py               # Giao diện người dùng Streamlit
└── README.md                # Hướng dẫn dự án và Link Demo
🚀 Hướng dẫn khởi chạy
1. Hướng dẫn cài đặt Environment
Mở Terminal tại thư mục gốc dự án và cài đặt các thư viện cần thiết bằng lệnh:

pip install fastapi uvicorn requests firebase-admin streamlit python-multipart
2. Hướng dẫn chạy Backend
Mở Terminal và thực thi chuỗi lệnh sau để khởi động server FastAPI:

PowerShell
$env:PYTHONPATH = "."
uvicorn backend.app.main:app --reload
Sau khi chạy, bạn có thể kiểm tra tài liệu API tự động tại: http://127.0.0.1:8000/docs

3. Hướng dẫn chạy Frontend
Mở một Terminal mới (vẫn giữ Terminal Backend đang chạy) và thực thi lệnh:

PowerShell
streamlit run frontend/app.py
📝 Thông tin sinh viên
Họ và tên: Hồ Tất Thành

Đơn vị: Trường Đại học Khoa học Tự nhiên - ĐHQG-HCM (VNUHCM-US)

Đồ án: Xây dựng API và tích hợp Firebase cho ứng dụng quản lý chi tiêu.
## 📺 Demo Video
**Đường dẫn xem Video Demo:** [👉 ]