import streamlit as st
from extracted_data_store import add_data, get_data
import process.chat_bot_helper as bot_helper


def load_context_and_chain():
    try:
        para_text = get_data("ext_text")
        if para_text is None:
            normal_chain = bot_helper.get_normal_chain()
            return normal_chain

        print("Para Text:", para_text)
        chain = bot_helper.create_context(para_text)
        return chain
    except KeyError as e:
        st.exception(f"Error: The key was not found in the data store. Details: {e}")
        return None
    except ValueError as e:
        st.exception(f"Error: {e}")
        return None
    except Exception as e:
        st.exception(f"An unexpected error occurred: {e}")
        return None


def chat_page():
    st.title("Echo Bot")
    chain = load_context_and_chain()
    print(
        "Successfully Load Chain -----------------------------------------------------"
    )

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

        para_text = get_data("ext_text")
        if para_text is None:
            response = bot_helper.get_normal_response(chain, prompt)
        else:
            response = bot_helper.get_response(chain, prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
