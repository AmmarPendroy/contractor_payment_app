import streamlit as st

st.set_page_config(page_title="Help & Instructions", layout="wide")

from utils.ui import render_header
render_header()

if "user" in st.session_state:
    role = st.session_state.user["role"]
    if role == "admin":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E6F0FF; }</style>', unsafe_allow_html=True)
    elif role == "contractor":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E8F8F0; }</style>', unsafe_allow_html=True)

st.title("📖 Welcome to the Contractor Payment System")

st.markdown("""
This portal allows **registered contractors** to:
- Submit payment requests 💰
- Upload supporting documents 📄
- Track request status ✅

### 💡 For Contractors:
1. Register with your **@geg-construction.com** email.
2. Wait for admin approval.
3. Navigate to **Submit Request** and attach your documents.

### 🛠 For Admins:
- Review incoming requests
- Approve or reject with one click
- Manage user accounts and roles
- Export data and analyze stats

Need help? Contact: `support@geg-construction.com`
""")
