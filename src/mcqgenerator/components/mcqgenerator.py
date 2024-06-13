import os ,sys ,json ,traceback 
import pandas as pd 
from dotenv import load_dotenv 
from src.mcqgenerator.logger.logger import logging 
from src.mcqgenerator.exception import MCQGeneratorException
from src.mcqgenerator.constant import *

from langchain.chat_models import ChatOpenAI 
from langchain.llms import OpenAI 
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain 
from langchain.chains import SequentialChain 
from langchain.callbacks import get_openai_callback
import PyPDF2
llm = ChatOpenAI(openai_api_key= KEY , model =MODEL ,temperature = TEMPERATURE)

def get_input_prompt():
    try:
        TEMPLATE="""
                Text:{text}
                You are an expert MCQ maker. Given the above text, it is your job to \
                create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
                Make sure the questions are not repeated and check all the questions to be conforming the text as well.
                Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
                Ensure to make {number} MCQs
                ### RESPONSE_JSON
                {response_json}

                """ 
        quiz_generation_prompt = PromptTemplate(
                    input_variables=['text' ,'number' ,'subject' ,'tone' ,'response_json'] ,
                    template = TEMPLATE
                   )
        return quiz_generation_prompt
    except Exception as e:
        raise MCQGeneratorException(e ,sys) from e


def get_output_prompt():
    try:
        TEMPLATE2="""
            You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
            You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
            if the quiz is not at per with the cognitive and analytical abilities of the students,\
            update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
            Quiz_MCQs:
            {quiz}

            Check from an expert English Writer of the above quiz:
            """ 
        quiz_evzluation_prompt = PromptTemplate(
                input_variables=['subject' ,'quiz'] ,
                template = TEMPLATE2
            ) 
        return quiz_evzluation_prompt

    except Exception as e:
        raise MCQGeneratorException(e ,sys) from e



def get_final_chain():
    try:
        quiz_generation_prompt = get_input_prompt()
        quiz_chain = LLMChain(llm= llm ,prompt= quiz_generation_prompt ,output_key='quiz' ,verbose=True)

        quiz_evzluation_prompt = get_output_prompt()
        review_chain = LLMChain(llm=llm ,prompt= quiz_evzluation_prompt ,output_key='review' ,verbose=True)

        generate_evaluation_chain = SequentialChain(
            chains=[quiz_chain , review_chain ] ,input_variables=['text' ,'number' ,'subject' ,'tone' ,'response_json'],
            output_variables=["quiz", "review"], verbose=True) 
        
        return generate_evaluation_chain
    except Exception as e:
        raise MCQGeneratorException(e ,sys) from e
