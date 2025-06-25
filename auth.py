import streamlit as st

def login():
    st.sidebar.title("🔐 Đăng nhập")
    username = st.sidebar.text_input("Tài khoản")
    password = st.sidebar.text_input("Mật khẩu", type="password")
    login_button = st.sidebar.button("Đăng nhập")

    if login_button:
        if username == "admin" and password == "123456":
            st.session_state["logged_in"] = True
            st.success("Đăng nhập thành công!")
        else:
            st.error("Sai tài khoản hoặc mật khẩu.")

    return st.session_state.get("logged_in", False)
