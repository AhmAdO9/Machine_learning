import setuptools
from typing import List


HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path, "r") as file_object:
        requirements = file_object.readlines()
        requirement = [req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirement:
            requirement.remove(HYPHEN_E_DOT)
    
    return requirement



__version__ = "0.0.0"

REPO_NAME = "Machine_learning"
AUTHOR_USER_NAME = "AhmAdO9"
SRC_REPO = "Cnn_Classifier"
AUTHOR_EMAIL = "adahm7114@gmail.com"

setuptools.setup(

    name = SRC_REPO,
    version = __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires = get_requirements('requirements.txt')

)
