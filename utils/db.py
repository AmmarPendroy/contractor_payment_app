import streamlit as st
from firebase_config import db, storage
import datetime
import uuid

def upload_documents(files, uid):
    file_urls = []
    for file in files:
        file_id = f"{uid}/{uuid.uuid4()}_{file.name}"
        storage.child(file_id).put(file)
        url = storage.child(file_id).get_url(None)
        file_urls.append(url)
    return file_urls

def submit_payment_request(contractor, amount, period, description, files):
    uid = st.session_state.user["uid"]
    start_date = str(period[0])
    end_date = str(period[1])

    urls = upload_documents(files, uid) if files else []

    payload = {
        "contractor": contractor,
        "amount": amount,
        "description": description,
        "work_period": {
            "start": start_date,
            "end": end_date
        },
        "documents": urls,
        "status": "pending",
        "submitted_at": str(datetime.datetime.now()),
        "user_id": uid
    }

    db.child("payment_requests").push(payload)
    st.success("✅ Payment request submitted successfully!")

def get_all_requests(status_filter=None):
    all_reqs = db.child("payment_requests").get().val() or {}
    if status_filter:
        return {k: v for k, v in all_reqs.items() if v.get("status") == status_filter}
    return all_reqs

def get_user_requests(uid):
    all_reqs = db.child("payment_requests").get().val() or {}
    user_reqs = [v for v in all_reqs.values() if v.get("user_id") == uid]
    return sorted(user_reqs, key=lambda x: x["submitted_at"])

def get_all_users():
    return db.child("users").get().val() or {}

def update_user_status(uid, status):
    db.child("users").child(uid).update({
        "status": status,
        "updated_at": str(datetime.datetime.now())
    })

def reset_user_password(email):
    from firebase_config import auth
    try:
        auth.send_password_reset_email(email)
        st.success(f"Password reset email sent to {email}")
    except:
        st.error("Failed to send password reset email.")

from utils.emailer import send_email
send_email(
    subject="New Payment Request Submitted",
    message=f"New request from {contractor} for ${amount}.\n\nCheck dashboard to review.",
    to_email=st.secrets["email"]["notify_admin"]
)
