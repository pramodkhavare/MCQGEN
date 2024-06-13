from dotenv import load_dotenv 
import os,sys

load_dotenv()  #This function will help you to load local environment which yocreated using .env file
KEY = os.getenv("OPENAI_API_KEYS")
 

MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0.5 
RESPONSE_JSON_PATH = r"C:\Users\PRAMOD KHAVARE\MCQGEN\config\Response.json"

