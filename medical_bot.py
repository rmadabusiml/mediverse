import os
import streamlit as st
import requests as req
from datetime import datetime
import re

HTTP_OK = 200
api = os.environ.get("FOO")

st.write(f"api is {api}")

if api is None:
    api = "https://204iebgau9.execute-api.us-east-1.amazonaws.com/prod/"

api_rag_ep = f"{api}/api/v1/llm/rag"

def display_medical_bot():
    st.title("👩‍💻 MediVerse Bot - A Virtual assistant for a medical knowledge base")
    st.warning('Please note each request will take at least 15 to 20 seconds to complete. Please see the details in the architecture on what happens behind the scene. Moreover, the backend is deployed on a conservative machine to keep the cost low. Please keep an eye on top right hand corner of the app to know the status of your request (eg: you should see a running animation)', icon="⚠️")

    # Get user input
    user_input = st.text_area("You:", key="input", placeholder="Ask me a question... (navigate to sample prompts section for sample questions to ask)")

    # Create columns for the buttons
    col1, col2 = st.columns(2)

    # Check if 'processing' key exists in session state
    if 'processing' not in st.session_state:
        st.session_state.processing = False

    # Submit button
    if col1.button("Submit", disabled=st.session_state.processing) or (user_input and user_input[-1] == "\n"):
        st.session_state.processing = True  # Set processing to True when button is clicked

        start_time = datetime.now()
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        data = {"q": user_input.strip(), "verbose": True}
        resp = req.post(api_rag_ep, headers=headers, json=data)
        end_time = datetime.now()
        time_taken = (end_time - start_time).total_seconds()

        if resp.status_code != HTTP_OK:
            output = resp.text
        else:
            resp = resp.json()
            output = f"{resp['answer']}"
            
            # Assuming the 'answer' string is structured as "Main answer text\n\nSources:[...]"
            # Split the answer string to extract main answer and sources
            main_answer, sources_str = output.split("\n\nSources:")
            
            # Display the main answer
            st.success(f"{main_answer}")
            st.subheader("Sources:")
            st.write(sources_str)
            st.write("---")

        st.session_state.setdefault("conversations", []).append((user_input, output, time_taken))
        st.session_state.processing = False  # Set processing to False after processing is done

    # Clear Chat History button
    if col2.button("Clear Chat History"):
        if 'conversations' in st.session_state:
            del st.session_state['conversations']
        st.experimental_rerun()  # Refresh the page

    # Display the conversation history
    if 'conversations' in st.session_state:
        for question, answer, duration in reversed(st.session_state["conversations"]):
            st.info(f"You: {question} (Took {duration:.2f} seconds)")
            st.success(f"Mediverse Bot: {answer}")
