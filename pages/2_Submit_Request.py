import streamlit as st
from utils.auth import ensure_logged_in
from utils.db import submit_payment_request
from datetime import date
from utils.ui import render_header
render_header()

if "user" in st.session_state:
    role = st.session_state.user["role"]
    if role == "admin":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E6F0FF; }</style>', unsafe_allow_html=True)
    elif role == "contractor":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E8F8F0; }</style>', unsafe_allow_html=True)

st.set_page_config(page_title="Submit Request", layout="centered")
ensure_logged_in(role="contractor")

st.title("📝 Submit Payment Request")

with st.form("payment_form", clear_on_submit=True):
    contractor_name = st.session_state.user.get("name") or st.session_state.user["email"]
    amount = st.number_input("Amount (USD)", min_value=1.0, step=0.5)
    work_period = st.date_input("Work Period", value=(date.today(), date.today()))
    description = st.text_area("Work Description / Notes")

    uploaded_files = st.file_uploader("Upload Supporting Documents (PDFs, Images)", type=["pdf", "png", "jpg"], accept_multiple_files=True)

    submitted = st.form_submit_button("📤 Submit Request")

    if submitted:
        submit_payment_request(
            contractor=contractor_name,
            amount=amount,
            period=work_period,
            description=description,
            files=uploaded_files
        )
