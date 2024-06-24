import streamlit as st
from extracted_data_store import add_data, get_data


# Define the next page UI
def chat_page():
    st.title("Next Page")
    st.write("This is the content of the next page.")
    para_text = get_data("ext_text")
    st.write(para_text)
    # Button to go back to the main page
    if st.button("Go Back"):
        st.session_state.page = "pdf"
