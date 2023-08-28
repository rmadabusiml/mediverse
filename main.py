import streamlit as st
from medical_bot import display_medical_bot
from about import display_about
from sample_questions import display_sample_questions
from architecture import display_architecture

# Page title and layout
st.set_page_config(page_title='MediVerse - A Virtual assistant for medical knowledge base 👩‍💻', layout='wide')

# Sidebar
st.sidebar.image("medical-bot.png", width=250)  # Adjust the width as needed
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About", "Architecture", "Sample Prompts", "Medical Bot"])

# Main content
if page == "Medical Bot":
    display_medical_bot()
elif page == "About":
    display_about()
elif page == "Architecture":
    display_architecture()
elif page == "Sample Prompts":
    display_sample_questions()

