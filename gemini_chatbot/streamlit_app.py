import os
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from utils.loader import load_pdf_text, load_csv_text
import google.generativeai as genai
from dotenv import load_dotenv

# —————————————————————————————
# Authentication Setup
# Replace these values with your Azure AD App credentials
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
TENANT_ID = "YOUR_TENANT_ID"

credentials = {
    "azure": {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "tenant_id": TENANT_ID,
        "redirect_uri": "https://geministreamlitbot.azurewebsites.net",
    }
}

authenticator = stauth.AzureAuthenticator(credentials, login_button_name="Login with Azure AD")

user = authenticator.authenticate()
if not user:
    st.stop()  # Blocks further UI until login is successful
# —————————————————————————————

# Initialize Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

st.set_page_config(page_title="Gemini Chatbot with Azure AD SSO", layout="wide")
st.title("📄 Gemini Doc Chatbot + Azure AD SSO")

# Chat and upload logic …

