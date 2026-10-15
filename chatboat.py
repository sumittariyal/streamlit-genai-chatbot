import streamlit as st
from langchain_ollama import ChatOllama
llm = ChatOllama(
    model="llama3.2",
    temperature=0.0
)
# streamlit page setup

st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered"
)
st.title("💬 Generative AI Chatbot")
# initiate chat history

if 'chat_history' not in st.session_state:
    st.session_state.chat_history=[]
    
# show chat_history on the screen

for message in st.session_state.chat_history:
    # create a chat bubble and then there content
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input_box
user_prompt = st.chat_input("Ask Chatbot")

if user_prompt:
    # create a chat  bubble for user
    with st.chat_message("user"):  
        st.markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})
     
    response = llm.invoke(
        input= [{"role":"system","content":"You are a helpful assistant"},*st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})
    
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
