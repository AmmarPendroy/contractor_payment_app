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
            background-color: #ffffff;
            padding: 10px 20px;
            z-index: 999;
            border-bottom: 1px solid #ddd;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'Segoe UI', sans-serif;
        }
        .role-tag {
            font-size: 0.85rem;
            padding: 2px 10px;
            border-radius: 20px;
            font-weight: bold;
        }
        .admin-role {
            background-color: #007BFF;
            color: white;
        }
        .contractor-role {
            background-color: #28A745;
            color: white;
        }
        .notif-badge {
            background-color: red;
            color: white;
            padding: 4px 8px;
            border-radius: 999px;
            font-size: 0.75rem;
            margin-left: 8px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    user = st.session_state.get("user")
    if not user:
        return

    role = user.get("role", "contractor").lower()
    email = user.get("email", "")

    notif_count = 0
    if role == "admin":
        pending = get_all_requests(status_filter="pending")
        notif_count = len(pending)

    role_color = "admin-role" if role == "admin" else "contractor-role"
    notif_html = f'<span class="notif-badge">{notif_count}</span>' if notif_count > 0 else ""

    st.markdown(
        f"""
        <div class="app-header">
            <div>👤 <strong>{email}</strong></div>
            <div>
                <span class="role-tag {role_color}">{role.title()}</span>
                {notif_html}
            </div>
        </div>
        <br><br><br>
        """, unsafe_allow_html=True
    )
