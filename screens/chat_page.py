import streamlit as st


# Define the next page UI
def chat_page():
    st.title("Next Page")
    st.write("This is the content of the next page.")
    # Button to go back to the main page
    if st.button("Go Back"):
        st.session_state.page = "main"
