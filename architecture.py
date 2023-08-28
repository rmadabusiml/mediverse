import streamlit as st

def display_architecture():
    st.title("Design & Architecture of Mediverse Bot")
    
    st.header("LLM & RAGs")
    contexts = [
        "Large Language Models (LLMs) have ushered in a new era of conversational AI, enabling chatbots to engage in human-like dialogues across diverse subjects. However, while LLMs are linguistically adept, they sometimes struggle with highly specialized topics or up-to-date information. To address this, developers are integrating LLMs with specific data sources, allowing them to tap into internal knowledge bases. This fusion of general linguistic prowess with specialized knowledge ensures that chatbots can provide accurate answers without resorting to guesswork.",
        "One of the innovative techniques employed in this integration is the use of Retrieval-Augmented Generation (RAG). RAG combines the strengths of retrieval-based and generative approaches, allowing the model to pull relevant information from a database and then generate a coherent response. The data, often in the form of text files, is transformed into embedding vectors, which are essentially numerical representations capturing the essence of the information. These vectors are crucial as they allow for efficient storage and quick retrieval of data, ensuring that the chatbot's responses are both prompt and pertinent.",
        "The process of building such a sophisticated chatbot involves several stages. After data extraction, where relevant documents are gathered, the initialization phase begins. This involves loading the data, creating embeddings, and setting up an index. With tools available today, developers can even pull data from diverse sources, including scientific repositories. Once the data is vectorized and stored, the LLM can then use it for inference, ensuring that the responses generated are not only linguistically sound but also factually accurate and contextually relevant."
    ]
    for context in contexts:
        st.markdown(f"- {context}")
    
    # Design
    st.header("High-level Design of Mediverse Bot")
    st.image("hu_design.png", width=750) 
    
    # Architecture
    st.header("Architecture of Mediverse Bot on Amazon Web Services (AWS)")
    st.image("hu_architecture.png", width=750) 
    

