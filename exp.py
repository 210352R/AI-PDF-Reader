import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="Navigation Example", page_icon=":arrow_right:")


# Define the main page UI
def main():
    st.title("Main Page")
    st.write("This is the main page content.")
    # Button to navigate to the next page
    if st.button("Go to Next Page"):
        st.session_state.page = "next"


# Define the next page UI
def next_page():
    st.title("Next Page")
    st.write("This is the content of the next page.")
    # Button to go back to the main page
    if st.button("Go Back"):
        st.session_state.page = "main"


# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "main"

# Route to the appropriate page based on the session state
if st.session_state.page == "main":
    main()
elif st.session_state.page == "next":
    next_page()
