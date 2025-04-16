import streamlit as st
import os, sys

st.set_page_config(page_title="Register", layout="centered")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.auth import register_user
from utils.ui import render_header

render_header()

st.title("📝 Register")

email = st.text_input("Email", key="register_email")
password = st.text_input("Password", type="password", key="register_password")
role = st.selectbox("Select Role", ["contractor", "admin"], key="register_role")

if st.button("Register"):
    register_user(email, password, role)

if "user" in st.session_state:
    role = st.session_state.user.get("role")
    if role == "admin":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E6F0FF; }</style>', unsafe_allow_html=True)
    elif role == "contractor":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E8F8F0; }</style>', unsafe_allow_html=True)
