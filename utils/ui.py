import streamlit as st

def render_header():
    st.markdown("""
        <div style='background-color: #004080; padding: 1rem; border-radius: 10px;'>
            <h1 style='color: white; text-align: center;'>Contractor Payment System</h1>
        </div>
    """, unsafe_allow_html=True)
