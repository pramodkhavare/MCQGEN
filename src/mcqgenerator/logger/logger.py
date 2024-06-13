
import logging 
import os ,sys
from datetime import datetime
import pandas as pd
LOG_DIR = 'MCQGEN'
LOG_DIR = os.path.join(os.getcwd() , LOG_DIR)

os.makedirs(LOG_DIR , exist_ok=True)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"

file_name = f"log_{CURRENT_TIME_STAMP}.log"

log_file_path = os.path.join(LOG_DIR , file_name)

logging.basicConfig(filename=log_file_path ,
                    filemode= 'w',
                    format= '[%(asctime)s] %(lineno)d %(name)s -%(levelname)s -%(message)s',
                    level=logging.INFO
                    )


# def get_log_dataframe(file_path):
#     data=[]
#     with open(file_path) as log_file:
#         for line in log_file.readlines():
#             data.append(line.split("^;"))

#     log_df = pd.DataFrame(data)
#     columns=["Time stamp","Log Level","line number","file name","function name","message"]
#     log_df.columns=columns
    
#     log_df["log_message"] = log_df['Time stamp'].astype(str) +":$"+ log_df["message"]

#     return log_df[["log_message"]]
