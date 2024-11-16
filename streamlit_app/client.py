import requests
import streamlit as st

# Openai
def get_openai_response(input_text, input_type):
    if input_type=="essay":
        if(input_text != "" and input_text != None):
            response=requests.post(
                "http://localhost:8000/openai/essay/invoke",
                json={'input':{'topic':input_text}}
            )
            return response.json()['output']['content']

    elif input_type=="poem":
        if(input_text != "" and input_text != None):
            response=requests.post(
                "http://localhost:8000/openai/poem/invoke",
                json={'input':{'topic':input_text}}
            )
            return response.json()['output']['content']
    else:
        return None
# Ollama
def get_ollama_response(input_text, input_type):
    if input_type=="essay":
        if(input_text != "" and input_text != None):
            response=requests.post(
                "http://localhost:8000/ollama/essay/invoke",
                json={'input':{'topic':input_text}}
            )
            return response.json()['output']

    elif input_type=="poem":
        if(input_text != "" and input_text != None):
            response=requests.post(
                "http://localhost:8000/ollama/poem/invoke",
                json={'input':{'topic':input_text}}
            )
            return response.json()['output']
    else:
        return None

st.html("<h2>Langchain Demo With Ollama and Openai</h2>")

option_1 = st.selectbox(
    "Select Api type :",
    ("Ollama", "Openai"),
)
option_2 = st.selectbox(
    "Select prompt type :",
    ("essay", "poem"),
)

if option_1 == "Ollama":
    input_text = st.text_input(f"({option_1})Write an {option_2} on", placeholder="Ex: apple", key='widget')
    st.text_area(label="", value=get_ollama_response(st.session_state.widget, option_2))
    st.session_state.input_text = ""

elif option_1 == "Openai":
    input_text = st.text_input(f"({option_1})Write an {option_2} on", placeholder="Ex: apple", key='widget')
    st.text_area(label="", value=get_openai_response(st.session_state.widget, option_2))
    st.session_state.input_text = ""
