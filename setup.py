from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "mcqgenerator" 
VERSION = "0.0.1"
DESCRIPTION = "This is modular coding project used for Generating MCQ"
AUTHOR_NAME = "Pramod Khavare"
AUTHOR_EMIL = "pramodkhavare2000@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."
# Requriments.txt file open
# read
# \n ""
def get_requirements_list()->List[str]:
    """
    This function going to list of library name 
    in requirements.txt file 

    return type : List[str]
    """
    with open(REQUIREMENTS_FILE_NAME) as requriment_file:
        requriment_list = requriment_file.readlines()
        requriment_list = [requriment_name.replace("\n", "") for requriment_name in requriment_list]

        if HYPHEN_E_DOT in requriment_list:
            requriment_list.remove(HYPHEN_E_DOT)

        return requriment_list

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMIL,
      packages=find_packages(),
      install_requries = get_requirements_list()
     )


if __name__ == "__main__":
    print(get_requirements_list())