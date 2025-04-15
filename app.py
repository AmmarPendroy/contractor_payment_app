import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Contractor Payment System",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .main {padding-top: 2rem;}
    .stButton button {
        border-radius: 0.5rem;
        font-size: 1rem;
        padding: 0.75rem 1.5rem;
    }
    .stTextInput input, .stSelectbox div {
        font-size: 1rem;
        padding: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚧 Contractor Payment Portal")

st.markdown("Welcome! Please navigate using the tabs on the left.")

if "user" in st.session_state:
    role = st.session_state["user"]["role"]
    if role == "admin":
        switch_page("Review_Requests")
    else:
        switch_page("Submit_Request")
else:
    switch_page("Login")

