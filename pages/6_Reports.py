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

st.set_page_config(page_title="Reports & Export", layout="wide")
ensure_logged_in(role="admin")

st.title("📊 Reports & Export")

data_dict = get_all_requests()
if not data_dict:
    st.info("No payment records found.")
    st.stop()

df = pd.DataFrame(data_dict).T
df["submitted_at"] = pd.to_datetime(df["submitted_at"])
df["work_start"] = pd.to_datetime(df["work_period"].apply(lambda x: x["start"]))
df["work_end"] = pd.to_datetime(df["work_period"].apply(lambda x: x["end"]))

with st.sidebar:
    st.header("🔎 Filter")
    status_filter = st.multiselect("Status", options=df["status"].unique(), default=list(df["status"].unique()))
    contractor_filter = st.multiselect("Contractor", options=df["contractor"].unique(), default=list(df["contractor"].unique()))
    date_range = st.date_input("Work Period", [])

filtered_df = df[
    (df["status"].isin(status_filter)) &
    (df["contractor"].isin(contractor_filter))
]

if date_range and len(date_range) == 2:
    filtered_df = filtered_df[
        (filtered_df["work_start"] >= pd.to_datetime(date_range[0])) &
        (filtered_df["work_end"] <= pd.to_datetime(date_range[1]))
    ]

st.subheader("📈 Summary Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Total Requests", len(filtered_df))
col2.metric("Total Amount", f"${filtered_df['amount'].sum():,.2f}")
col3.metric("Approved Amount", f"${filtered_df[filtered_df['status'] == 'approved']['amount'].sum():,.2f}")

fig = px.histogram(filtered_df, x="contractor", y="amount", color="status", barmode="group", title="Amounts by Contractor")
st.plotly_chart(fig, use_container_width=True)

fig2 = px.pie(filtered_df, names="status", title="Status Distribution")
st.plotly_chart(fig2, use_container_width=True)

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download CSV", data=csv, file_name="payment_report.csv", mime="text/csv")
