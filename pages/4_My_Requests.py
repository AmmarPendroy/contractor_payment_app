from utils.ui import render_header
render_header()

import streamlit as st
from utils.auth import ensure_logged_in
from utils.db import get_user_requests

st.set_page_config(page_title="My Requests", layout="wide")
ensure_logged_in(role="contractor")

st.title("📄 My Payment Requests")

requests = get_user_requests(st.session_state.user["uid"])

if not requests:
    st.info("No submissions yet.")
else:
    for req in reversed(requests):  # latest first
        status = req.get("status", "unknown").capitalize()
        status_color = {
            "Pending": "orange",
            "Approved": "green",
            "Rejected": "red"
        }.get(status, "gray")

        with st.expander(f"💰 ${req['amount']} | {req['work_period']['start']} to {req['work_period']['end']} | [{status}]", expanded=False):
            st.markdown(f"**Description:** {req['description']}")
            st.markdown(f"**Submitted At:** {req['submitted_at']}")

            if req.get("reviewed_at"):
                st.markdown(f"**Reviewed At:** {req['reviewed_at']}")
                st.markdown(f"**Reviewer:** {req['reviewer']}")

            st.markdown(f"<span style='color:{status_color}; font-weight:bold;'>Status: {status}</span>", unsafe_allow_html=True)

            if req.get("documents"):
                st.markdown("**Attached Documents:**")
                for url in req["documents"]:
                    st.markdown(f"[📎 View File]({url})", unsafe_allow_html=True)
