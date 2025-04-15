import streamlit as st
from utils.auth import ensure_logged_in
from utils.db import get_all_requests, update_request_status
from utils.ui import render_header
render_header()

if "user" in st.session_state:
    role = st.session_state.user["role"]
    if role == "admin":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E6F0FF; }</style>', unsafe_allow_html=True)
    elif role == "contractor":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E8F8F0; }</style>', unsafe_allow_html=True)

st.set_page_config(page_title="Review Requests", layout="wide")
ensure_logged_in(role="admin")

st.title("🗂 Review Payment Requests")

requests = get_all_requests(status_filter="pending")

if not requests:
    st.info("No pending requests at the moment.")
else:
    for req_id, req in requests.items():
        with st.expander(f"{req['contractor']} – ${req['amount']} – {req['work_period']['start']} to {req['work_period']['end']}"):
            st.write(f"**Description:** {req['description']}")
            st.write(f"**Submitted At:** {req['submitted_at']}")

            if req.get("documents"):
                st.markdown("**Attached Documents:**")
                for url in req["documents"]:
                    st.markdown(f"[📎 View File]({url})", unsafe_allow_html=True)

            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("✅ Approve", key=f"approve_{req_id}"):
                    update_request_status(req_id, "approved")
                    st.success("Approved!")
                    st.experimental_rerun()

            with col2:
                if st.button("❌ Reject", key=f"reject_{req_id}"):
                    update_request_status(req_id, "rejected")
                    st.warning("Rejected.")
                    st.experimental_rerun()
