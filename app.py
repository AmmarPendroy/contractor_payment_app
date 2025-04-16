import streamlit as st
from utils.ui import render_header
render_header()

st.set_page_config(
    page_title="Contractor Payment System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Role-based sidebar color
if "user" in st.session_state:
    role = st.session_state.user["role"]
    if role == "admin":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E6F0FF; }</style>', unsafe_allow_html=True)
    elif role == "contractor":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E8F8F0; }</style>', unsafe_allow_html=True)

# Header
st.title("🚧 Contractor Payment Portal")
st.markdown("Use the sidebar to navigate the system.")

# Sidebar nav
st.sidebar.title("📂 Navigation")
selection = st.sidebar.radio("Go to", options=[
    "Help",
    "Login/Register",
    "Submit Request",
    "My Requests",
    "Review Requests",
    "User Management",
    "Reports",
    "Site Charts"
])

# Simple prompt
if "user" not in st.session_state:
    st.warning("You're not logged in. Please use the sidebar to go to **Login**.")
else:
    st.success(f"Logged in as {st.session_state.user['email']} ({st.session_state.user['role'].title()})")
