from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    """This Funtion will return list of requirements. """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)




setup(
name = "mlproject",
version="0.0.1",
author="Rohit",
author_email="mail.rohit.kmr@gmail.com",
packages=find_packages(),
install_reqires=get_requirements("requirements.txt")

)