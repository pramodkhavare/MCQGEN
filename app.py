import os ,sys ,json ,traceback 
import pandas as pd 
from dotenv import load_dotenv 
from langchain.callbacks import get_openai_callback
import streamlit as st 

from src.mcqgenerator.utils.utils import read_file ,get_table_data_from_quiz 
from src.mcqgenerator.logger.logger import logging
from src.mcqgenerator.exception import MCQGeneratorException
from src.mcqgenerator.constant import * 
from src.mcqgenerator.components.mcqgenerator import get_final_chain
from langchain.chat_models import ChatOpenAI 
from langchain.llms import OpenAI 
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain 
from langchain.chains import SequentialChain 

# Load RESPONSE_JSON
try:
    with open(RESPONSE_JSON_PATH, 'r') as file:
        RESPONSE_JSON = json.load(file)
except Exception as e:
    st.error(f"Error loading RESPONSE_JSON: {e}")
    RESPONSE_JSON = {}


# Create a title for the app
st.title("*****MCQ Generator Application with LangChain*****")

# Accept File using st.form
with st.form("User_Input"):
    # File Upload
    uploaded_file = st.file_uploader("Upload a PDF or txt File", type=["pdf", "txt"])
    # Input Fields
    # 1. MCQ
    mcq_counts = st.number_input("No of MCQs", min_value=3, max_value=50)

    # 2. Subject
    subject = st.text_input("Insert Subject", max_chars=30)

    # 3. Tone
    tone = st.text_input("Complexity level of Subject", max_chars=30, placeholder='Simple')

    # Submit Button
    button = st.form_submit_button('Create MCQs')

    if button and uploaded_file is not None and mcq_counts and subject and tone:
        with st.spinner('loading.....'):
            try:
                text = read_file(uploaded_file)
                generate_evaluation_chain = get_final_chain()
                with get_openai_callback() as cb:
                    response = generate_evaluation_chain(
                        {
                            'text': text,
                            'number': mcq_counts,
                            'subject': subject,
                            'tone': tone,
                            'response_json': json.dumps(RESPONSE_JSON)
                        }
                    )
                    
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error('Error')
            else:
                if isinstance(response, dict):
                    response_quiz = response.get('quiz', None)

                    if response_quiz:
                        try:
                            table_data = get_table_data_from_quiz(dict_string=response_quiz)
                            if table_data is not None:
                                df = pd.DataFrame(table_data)
                                df.index = df.index + 1
                                st.table(df)
                                st.text_area(label='Review', value=response['review'])
                            else:
                                st.error('Error in table data')
                        except json.JSONDecodeError as e:
                            st.error(f"Error decoding JSON: {e}")
                    else:
                        st.error('Quiz data is missing')
                else:
                    st.write(response)








