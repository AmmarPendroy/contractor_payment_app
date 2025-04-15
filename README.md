# 🚧 Contractor Payment System (Streamlit + Firebase)

A role-based system for GEG contractors to submit and track payment requests.

## 🔧 Features
- Contractor login and submission
- File uploads (PDF, images)
- Admin dashboard to approve/reject
- In-app notifications & email alerts
- Regional analytics + export
- Audit logging
- Mobile-friendly UI with role themes

## 🚀 Deploy on Streamlit Cloud

### 1. Create `.streamlit/secrets.toml` and `.streamlit/config.toml`
Follow `secrets.toml` format to paste your Firebase and Gmail settings.

### 2. Push to GitHub

### 3. Deploy
Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) → "New App" → Choose your GitHub repo → Set main file: `app.py`.

### 4. Login Only with:
Emails ending in `@geg-construction.com`

---

## 🛠 Firebase Setup

- Realtime DB + Storage: enabled
- Email/Password auth: enabled
- Create Web App → Get API keys for config

---

Need help? Email: support@geg-construction.com
