import streamlit as st
from utils.auth import ensure_logged_in
from utils.db import get_all_requests
import pandas as pd
import plotly.express as px
from utils.ui import render_header
render_header()

if "user" in st.session_state:
    role = st.session_state.user["role"]
    if role == "admin":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E6F0FF; }</style>', unsafe_allow_html=True)
    elif role == "contractor":
        st.markdown('<style>.sidebar .sidebar-content { background-color: #E8F8F0; }</style>', unsafe_allow_html=True)

st.set_page_config(page_title="Site Reports", layout="wide")
ensure_logged_in(role="admin")

st.title("📍 Site / Region Analytics")

requests = get_all_requests()
if not requests:
    st.warning("No data available.")
    st.stop()

df = pd.DataFrame(requests).T
df["submitted_at"] = pd.to_datetime(df["submitted_at"])
df["contractor"] = df["contractor"].astype(str)

# Assume contractor names like "ZAS - Ali", extract site prefix
df["site"] = df["contractor"].apply(lambda x: x.split(" - ")[0] if " - " in x else "Unknown")

st.subheader("💰 Amounts by Site")
fig = px.bar(df, x="site", y="amount", color="status", barmode="group")
st.plotly_chart(fig, use_container_width=True)

st.subheader("📈 Submissions Over Time")
fig2 = px.histogram(df, x="submitted_at", color="site")
st.plotly_chart(fig2, use_container_width=True)
