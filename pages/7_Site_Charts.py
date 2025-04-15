import streamlit as st
from utils.auth import ensure_logged_in
from utils.db import get_all_requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Site Reports", layout="wide")
from utils.ui import render_header
render_header()
ensure_logged_in(role="admin")

st.title("📍 Site / Region Analytics")

requests = get_all_requests()
if not requests:
    st.warning("No data available.")
    st.stop()

df = pd.DataFrame(requests).T
df["submitted_at"] = pd.to_datetime(df["submitted_at"])
df["contractor"] = df["contractor"].astype(str)

# Dummy extraction: assume site is part of contractor name, e.g., "ZAS - Ali"
df["site"] = df["contractor"].apply(lambda x: x.split(" - ")[0] if " - " in x else "Unknown")

st.subheader("💰 Amounts by Site")
fig = px.bar(df, x="site", y="amount", color="status", barmode="group")
st.plotly_chart(fig, use_container_width=True)

st.subheader("📈 Submissions Over Time")
fig2 = px.histogram(df, x="submitted_at", color="site")
st.plotly_chart(fig2, use_container_width=True)
