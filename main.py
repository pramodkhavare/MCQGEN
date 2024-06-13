import streamlit as st 
import os ,sys ,json ,traceback 
import pandas as pd 
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.utils.utils import read_file ,get_table_data_from_quiz 
from src.mcqgenerator.components.mcqgenerator import get_final_chain
from src.mcqgenerator.constant import * 
try:
    with open(RESPONSE_JSON_PATH, 'r') as file:
        RESPONSE_JSON = json.load(file)
except Exception as e:
    st.error(f"Error loading RESPONSE_JSON: {e}")
    RESPONSE_JSON = {}
with st.form("User_Input"):
    # File Upload
    uploaded_file = st.file_uploader("Upload a PDF or txt File", type=["pdf", "txt"])

    button = st.form_submit_button('Create MCQs')
    text = read_file(uploaded_file)

    generate_evaluation_chain = get_final_chain()
    with get_openai_callback() as cb:
                    response = generate_evaluation_chain(
                        {
                            'text': text,
                            'number': 3,
                            'subject': "English",
                            'tone': "Simple",
                            'response_json': json.dumps(RESPONSE_JSON)
                       
                        }
                    )
    print('PRAMODDNDDFDDUFUD')
    print(type(response))
    response_quiz = response.get('quiz', None)
    # response_quiz = json.loads(response_quiz)
    table_data = get_table_data_from_quiz(dict_string=response_quiz)
    