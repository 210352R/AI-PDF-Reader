import streamlit as st
from extracted_data_store import add_data, get_data


# # Define the next page UI
# def chat_page():
#     st.title("Chat Bot Page" ,     icon=":robot:face:")
#     st.write("This is the content of the next page.")
#     para_text = get_data("ext_text")
#     st.write(para_text)
#     # Button to go back to the main page
#     if st.button("Go Back"):
#         st.session_state.page = "pdf"


def chat_page():
    st.title("Echo Bot")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
