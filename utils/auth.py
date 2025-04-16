import streamlit as st
from firebase_config import auth, db
import datetime

SUPER_ADMIN_EMAIL = "ammar.muhammed@geg-construction.com"
SUPER_ADMIN_PASSWORD = "AmmarGEG99$"

def login_user(email, password):
    try:
        # Auto-login for super admin
        if email == SUPER_ADMIN_EMAIL and password == SUPER_ADMIN_PASSWORD:
            st.session_state.user = {
                "uid": "superadmin",
                "email": SUPER_ADMIN_EMAIL,
                "role": "admin",
                "name": "Super Admin",
                "status": "approved"
            }
            st.success("Logged in as Super Admin ✅")
            st.experimental_rerun()
            return

        # Normal login
        user = auth.sign_in_with_email_and_password(email, password)
        uid = user['localId']
        profile = db.child("users").child(uid).get().val()
        if not profile:
            st.error("User
