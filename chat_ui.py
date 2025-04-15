import streamlit as st
from rag_engine import load_rag_chain

st.set_page_config(page_title="DIT Campus Chatbot", page_icon="🎓")
st.title("🎓 DIT Campus Chatbot")

# Load RAG chain
rag_chain = load_rag_chain()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []  

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box for new message
user_input = st.chat_input("Ask me anything about the campus...")

# Handle user query
if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from RAG chain
    response = rag_chain.invoke({"input": user_input})
    answer = response["answer"]

    # Store and display assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
