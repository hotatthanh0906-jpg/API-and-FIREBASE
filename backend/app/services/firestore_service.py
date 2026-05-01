from backend.app.core.firebase_config import get_firestore
from datetime import datetime

db = get_firestore()

def save_expense(user_id: str, expense_data: dict):
    try:
        doc_ref = db.collection("expenses").document()
        data = {
            "user_id": user_id,
            "title": expense_data.get("title"),
            "amount": float(expense_data.get("amount", 0)),
            "category": expense_data.get("category"),
            "timestamp": datetime.now()
        }
        doc_ref.set(data)
        return doc_ref.id
    except Exception as e:
        print(f"❌ Error Saving: {e}")
        raise e

def load_expenses(user_id: str):
    try:
        expenses = []
        # Lấy dữ liệu lọc theo user_id (Bỏ order_by để tránh lỗi Index lúc demo)
        docs = db.collection("expenses").where("user_id", "==", user_id).stream()
        for doc in docs:
            item = doc.to_dict()
            item["id"] = doc.id
            if "timestamp" in item and item["timestamp"]:
                item["timestamp"] = str(item["timestamp"]) # Chuyển về string để dễ hiển thị
            expenses.append(item)
        return expenses
    except Exception as e:
        print(f"❌ Error Loading: {e}")
        return []