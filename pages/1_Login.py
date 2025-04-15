from utils.ui import render_header
render_header()

import streamlit as st
from utils.auth import login_user, register_user

st.set_page_config(page_title="Login", layout="centered")

st.title("🔐 Login to Your Account")

tab1, tab2 = st.tabs(["Login", "Register"])

with tab1:
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login_user(email, password)

with tab2:
    new_email = st.text_input("New Email")
    new_password = st.text_input("New Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")
    role = st.selectbox("Register as", ["Contractor", "Admin"])

    if st.button("Register"):
        if new_password == confirm:
            register_user(new_email, new_password, role.lower())
        else:
            st.warning("Passwords do not match.")
