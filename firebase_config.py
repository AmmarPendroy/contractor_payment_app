import pyrebase
import streamlit as st

# Firebase configuration pulled securely from .streamlit/secrets.toml
firebase_config = {
    "apiKey": st.secrets["firebase"]["api_key"],
    "authDomain": st.secrets["firebase"]["auth_domain"],
    "databaseURL": st.secrets["firebase"]["database_url"],
    "projectId": st.secrets["firebase"]["project_id"],
    "storageBucket": st.secrets["firebase"]["storage_bucket"],
