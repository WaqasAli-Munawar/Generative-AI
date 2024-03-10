
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("oapi_key")

client = OpenAI(api_key = api_key)

st.image("DS.png")
st.title("AI Advisor Bot :robot_face:")

with st.chat_message("ai"):
    st.write("How May I advice you today?")
    
    
user_input = st.chat_input("Please write your query")

if "conversatio_history" not in st.session_state:
    st.session_state["conversatio_history"] = []

conv_histroy = st.session_state["conversatio_history"]

if user_input is not None:
    conv_histroy.append({"sender":"user", "message": user_input})
    response = client.chat.completions.create(model = "gpt-3.5-turbo", messages = [{"role":"user", "content":user_input}])
    ai_response = response.choices[0].message.content
    conv_histroy.append({"sender":"ai", "message":ai_response})

for d in conv_histroy: # list of dictionary
    with st.chat_message(d["sender"]):
        st.write(d["message"])
        
if st.sidebar.button("clear history"):
    st.session_state["conversatio_history"] = []
