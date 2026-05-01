def add_expense(id_token: str, title: str, amount: float, category: str):
    r = requests.post(
        f"{API_BASE}/expenses/",
        json={"title": title, "amount": amount, "category": category},
        headers={"Authorization": f"Bearer {id_token}"}
    )
    r.raise_for_status()
    return r.json()

def get_expenses(id_token: str):
    r = requests.get(
        f"{API_BASE}/expenses/",
        headers={"Authorization": f"Bearer {id_token}"}
    )
    r.raise_for_status()
    return r.json()