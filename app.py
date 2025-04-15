import streamlit as st
from utils.ui import render_header
from utils.auth import get_current_user
from utils.sidebar import render_sidebar

# Render UI elements
render_sidebar()
render_header()

# Page routing
PAGES = {
    "Help": "pages/0_Help.py",
    "Login": "pages/1_Login.py",
    "Submit Request": "pages/2_Submit_Request.py",
    "Review Requests": "pages/3_Review_Requests.py",
    "My Requests": "pages/4_My_Requests.py",
    "Admin Users": "pages/5_Admin_Users.py",
    "Reports": "pages/6_Reports.py",
    "Site Charts": "pages/7_Site_Charts.py"
}

def main():
    st.set_page_config(page_title="Contractor Payment System", layout="wide")
    user = get_current_user()
    if user:
        st.switch_page(PAGES.get(st.session_state.get("current_page", "Submit Request")))
    else:
        st.switch_page(PAGES["Login"])

if __name__ == "__main__":
    main()
