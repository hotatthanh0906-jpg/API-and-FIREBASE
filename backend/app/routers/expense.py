from fastapi import APIRouter, Depends, HTTPException
from backend.app.dependencies.auth import get_current_user
from backend.app.schemas.expense import ExpenseCreate
from backend.app.services.firestore_service import save_expense, load_expenses

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/")
def add_expense(data: ExpenseCreate, user: dict = Depends(get_current_user)):
    try:
        expense_dict = {"title": data.title, "amount": data.amount, "category": data.category}
        save_expense(user["uid"], expense_dict)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def get_all_expenses(user: dict = Depends(get_current_user)):
    return load_expenses(user["uid"])