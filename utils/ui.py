import streamlit as st
from utils.db import get_all_requests

def render_header():
    st.markdown(
        """
        <style>
        .app-header {
            position: fixed;
            top: 0;
            width: 100%;
            background-color: #f9f9f9;
            padding: 10px 20px;
            z-index: 999;
            border-bottom: 1px solid #ccc;
        }
        .role-tag {
            font-size: 0.9rem;
            padding: 2px 8px;
            border-radius: 6px;
            background-color: #eee;
            color: #333;
            margin-left: 10px;
        }
        .notif-badge {
            background-color: red;
            color: white;
            padding: 2px 6px;
            border-radius: 999px;
            font-size: 0.75rem;
            margin-left: 6px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    user = st.session_state.get("user")
    if not user:
        return

    role = user.get("role", "contractor").capitalize()
    email = user.get("email", "")

    notif_count = 0
    if role.lower() == "admin":
        pending = get_all_requests(status_filter="pending")
        notif_count = len(pending)

    notif_html = f'<span class="notif-badge">{notif_count}</span>' if notif_count > 0 else ""
    st.markdown(f'<div class="app-header">👤 {email} <span class="role-tag">{role}</span> {notif_html}</div><br><br><br>', unsafe_allow_html=True)
