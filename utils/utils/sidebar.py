import streamlit as st

def render_sidebar():
    st.sidebar.title("📂 Navigation")

    if "user" in st.session_state:
        user = st.session_state.user
        role = user["role"]

        st.sidebar.markdown(f"👤 **{user['email']}**")
        st.sidebar.markdown(f"🔑 **Role**: `{role}`")

        if role == "admin":
            st.sidebar.page_link("pages/2_Submit_Request.py", label="📤 Submit Request")
            st.sidebar.page_link("pages/3_Review_Requests.py", label="🧐 Review Requests")
            st.sidebar.page_link("pages/4_My_Requests.py", label="📄 My Requests")
            st.sidebar.page_link("pages/5_Admin_Users.py", label="👥 Manage Users")
            st.sidebar.page_link("pages/6_Reports.py", label="📊 Reports")
            st.sidebar.page_link("pages/7_Site_Charts.py", label="📍 Site Charts")
        elif role == "contractor":
            st.sidebar.page_link("pages/2_Submit_Request.py", label="📤 Submit Request")
            st.sidebar.page_link("pages/4_My_Requests.py", label="📄 My Requests")

        st.sidebar.page_link("pages/0_Help.py", label="❓ Help")
        st.sidebar.button("🚪 Logout", on_click=logout_user)

    else:
        st.sidebar.page_link("pages/1a_Login.py", label="🔐 Login")
        st.sidebar.page_link("pages/1b_Register.py", label="📝 Register")
        st.sidebar.page_link("pages/0_Help.py", label="❓ Help")


def logout_user():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()
