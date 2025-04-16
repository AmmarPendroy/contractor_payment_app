import streamlit as st
from firebase_config import auth, db  ✅
import datetime

SUPER_ADMIN_EMAIL = "ammar.muhammed@geg-construction.com"
SUPER_ADMIN_PASSWORD = "AmmarGEG99$"

def login_user(email, password):
    try:
        # Super Admin shortcut login
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

        # Firebase login
        user = auth.sign_in_with_email_and_password(email, password)
        uid = user['localId']
        profile = db.child("users").child(uid).get().val()

        if not profile:
            st.error("User profile not found.")
            return

        if profile.get("status") != "approved":
            st.warning("Your account is not yet approved.")
            return

        st.session_state.user = {
            "uid": uid,
            "email": email,
            "role": profile.get("role", "contractor"),
            "name": profile.get("name", ""),
            "status": profile.get("status")
        }
        st.success("Logged in successfully!")
        st.experimental_rerun()
    except Exception as e:
        st.error("Login failed.")

def register_user(email, password, role):
    if not email.endswith("@geg-construction.com"):
        st.error("Only @geg-construction.com emails are allowed.")
        return
    try:
        user = auth.create_user_with_email_and_password(email, password)
        uid = user['localId']
        profile = {
            "email": email,
            "role": role,
            "status": "pending",
            "created_at": str(datetime.datetime.now())
        }
        db.child("users").child(uid).set(profile)
        st.success("Registration successful! Awaiting admin approval.")
    except Exception as e:
        st.error("Registration failed.")

def ensure_logged_in(role=None):
    if "user" not in st.session_state:
        st.error("Please log in to access this page.")
        st.stop()
    if role and st.session_state.user["role"] != role:
        st.error("Unauthorized access.")
        st.stop()
