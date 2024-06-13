import os ,sys ,json ,PyPDF2 ,traceback 
from src.mcqgenerator.logger.logger import logging 
from src.mcqgenerator.exception import MCQGeneratorException


def read_file(file):
    """
    This function will help to read file you get from streamlit only
    """
    try:
        if file.name.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(file)
            texts = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                texts += page.extract_text()
                print(texts)
                return texts
        
        elif file.name.endswith(".txt"):
            text = file.getvalue().decode('utf-8')
            print(text)
            return text
            
        else:
            raise MCQGeneratorException("Unsupported file format. Only PDF and text files are supported.", sys)
        
    except Exception as e:
        raise MCQGeneratorException(e ,sys) from e 
    

def get_table_data_from_quiz(dict_string):
    """
    You will pass string which have dictionary in it and you will get pandas DataFrame 
    """
    try:
        # Converting Data from String into Dict
        # quiz = json.loads(dict_string)
        if not dict_string:
            raise ValueError("Input string is empty or None")
        print(dict_string)
        response_quiz = json.loads(dict_string)
        quiz = response_quiz
        


        quiz_table_data = [] 
        for keys,items in quiz.items():
            mcq = items['mcq']
            options = (items['options'])
            options = " | | ".join([f"{key} : {value}" for key ,value in options.items()])

            correct = (items['correct'])
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
        return quiz_table_data
    except Exception as e:
        raise MCQGeneratorException(e ,sys) from e 