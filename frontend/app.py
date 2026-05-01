import streamlit as st
import requests

st.set_page_config(page_title="SmartSpend", page_icon="💰")
BACKEND_URL = "http://127.0.0.1:8000"

if 'user' not in st.session_state: st.session_state.user = None

def login_user(e, p):
    res = requests.post(f"{BACKEND_URL}/auth/login", json={"email": e, "password": p})
    if res.status_code == 200: return res.json()
    raise Exception(res.json().get("detail", "Lỗi"))

def register_user(e, p):
    res = requests.post(f"{BACKEND_URL}/auth/register", json={"email": e, "password": p})
    if res.status_code != 200: raise Exception(res.json().get("detail", "Lỗi"))

if not st.session_state.user:
    st.title("🔑 SmartSpend Login")
    with st.container(border=True):
        e = st.text_input("Email")
        p = st.text_input("Mật khẩu", type="password")
        c1, c2 = st.columns(2)
        if c1.button("Đăng nhập", use_container_width=True, type="primary"):
            try:
                st.session_state.user = login_user(e, p)
                st.rerun()
            except Exception as err: st.error(err)
        if c2.button("Đăng ký mới", use_container_width=True):
            try:
                register_user(e, p)
                st.success("Đăng ký xong! Hãy Đăng nhập.")
            except Exception as err: st.error(err)
else:
    with st.sidebar:
        st.write(f"👤 {st.session_state.user['email']}")
        if st.button("Đăng xuất"):
            st.session_state.user = None
            st.rerun()

    st.header("💰 Thêm khoản chi")
    with st.form("ex_form", clear_on_submit=True):
        t = st.text_input("Nội dung")
        a = st.number_input("Số tiền", min_value=0)
        c = st.selectbox("Loại", ["Ăn uống", "Di chuyển", "Mua sắm", "Khác"])
        if st.form_submit_button("Lưu"):
            headers = {"Authorization": f"Bearer {st.session_state.user['idToken']}"}
            res = requests.post(f"{BACKEND_URL}/expenses/", json={"title":t, "amount":a, "category":c}, headers=headers)
            if res.status_code == 200: 
                st.toast("Đã lưu!")
                st.rerun()

    st.header("📋 Lịch sử")
    headers = {"Authorization": f"Bearer {st.session_state.user['idToken']}"}
    data = requests.get(f"{BACKEND_URL}/expenses/", headers=headers).json()
    if data: st.dataframe(data, use_container_width=True)
    else: st.info("Chưa có dữ liệu.")