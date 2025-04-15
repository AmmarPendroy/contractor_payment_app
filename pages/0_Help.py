import streamlit as st
from utils.ui import render_header

st.set_page_config(page_title="Help & Instructions", layout="wide")
render_header()

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
