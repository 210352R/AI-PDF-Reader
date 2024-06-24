import streamlit as st
from pdfminer.high_level import extract_text
from screens.pdf_page import pdf_page
from screens.chat_page import chat_page

# Set page title and favicon
st.set_page_config(page_title="Upload PDF", page_icon=":robot_face:")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "chatbot"

# Route to the appropriate page based on the session state
if st.session_state.page == "pdf":
    pdf_page()

elif st.session_state.page == "chatbot":
    chat_page()
