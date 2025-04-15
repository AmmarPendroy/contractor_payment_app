import streamlit as st

st.set_page_config(
    page_title="Contractor Payment System",
    layout="wide",
    initial_sidebar_state="expanded"
)

from utils.ui import render_header
render_header()

# Sidebar coloring by role
if "user" in st.session_state:
    role = st.session_state.user["role"]
    if role == "admin":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E6F0FF; }</style>', unsafe_allow_html=True)
    elif role == "contractor":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E8F8F0; }</style>', unsafe_allow_html=True)

# Title
st.title("🚧 Contractor Payment Portal")
st.markdown("Use the sidebar to navigate the system.")

# Sidebar Nav
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

# Simple redirect notice
st.info(f"You selected: {selection}. Please navigate using the left panel tabs.")

# You can optionally preload values via query params
st.experimental_set_query_params(tab=selection.lower().replace(" ", "_"))
