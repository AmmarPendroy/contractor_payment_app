import streamlit as st
from utils.auth import ensure_logged_in
from utils.db import get_all_users, update_user_status, reset_user_password

st.set_page_config(page_title="User Management", layout="wide")
ensure_logged_in(role="admin")

st.title("👥 User Management")

users = get_all_users()

if not users:
    st.warning("No users found.")
else:
    for uid, user in users.items():
        status = user.get("status", "pending").capitalize()
        role = user.get("role", "contractor").capitalize()

        with st.expander(f"{user['email']} | {role} | Status: {status}"):
            st.markdown(f"**Email:** {user['email']}")
            st.markdown(f"**Role:** {role}")
            st.markdown(f"**Status:** {status}")
            st.markdown(f"**Created:** {user.get('created_at', 'N/A')}")

            col1, col2, col3 = st.columns(3)

            with col1:
                if st.button("✅ Approve", key=f"approve_{uid}"):
                    update_user_status(uid, "approved")
                    st.success("User approved.")
                    st.experimental_rerun()

            with col2:
                if st.button("❌ Reject", key=f"reject_{uid}"):
                    update_user_status(uid, "rejected")
                    st.warning("User rejected.")
                    st.experimental_rerun()

            with col3:
                if st.button("🔁 Reset Password", key=f"reset_{uid}"):
                    reset_user_password(user["email"])
