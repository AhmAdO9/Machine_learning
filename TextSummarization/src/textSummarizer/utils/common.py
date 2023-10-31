import os, json, yaml, base64, sys
from typing import Any
from box.exceptions import BoxValueError
from logger import logging
from exception import CustomException
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise CustomException(e, sys)
    

@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logging.info(f"Creating directory at: {path_to_directories}")


@ensure_annotations
def save_json(path:Path, data:dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path:Path):
    with open(path) as f:
        content = json.load(f)

    logging.info(f"json file loaded successfully")
    return ConfigBox(content)


@ensure_annotations
def getsize(path:Path):
    return round(os.path.getsize(path)/1024)


@ensure_annotations
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName,"wb") as f:
        f.write(imgdata)


@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    



