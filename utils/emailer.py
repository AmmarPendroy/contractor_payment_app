import smtplib
from email.mime.text import MIMEText
import streamlit as st

def send_email(subject, message, to_email):
    try:
        msg = MIMEText(message, "plain")
        msg["Subject"] = subject
        msg["From"] = st.secrets["email"]["sender"]
        msg["To"] = to_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(st.secrets["email"]["sender"], st.secrets["email"]["password"])
            server.send_message(msg)

        return True
    except Exception as e:
        st.error(f"❌ Email sending failed: {e}")
        return False
