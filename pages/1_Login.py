import streamlit as st

st.set_page_config(page_title="Login", layout="centered")

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.ui import render_header
render_header()

if "user" in st.session_state:
    role = st.session_state.user["role"]
    if role == "admin":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E6F0FF; }</style>', unsafe_allow_html=True)
    elif role == "contractor":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E8F8F0; }</style>', unsafe_allow_html=True)

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
