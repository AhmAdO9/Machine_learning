import os,sys
import urllib.request as request
import zipfile
from src.logger import logging
from Cnn_Classifier.utils.common import getsize
from ensure import ensure_annotations
from Cnn_Classifier.exception import CustomEx
import urllib.error
from Cnn_Classifier.constants import *
from Cnn_Classifier.utils.common import read_yaml, create_directories
from Cnn_Classifier.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    # def dowmnload_file(self):
    #     if not os.path.exists(self.config.local_data_file):
    #         filename, headers = request.urlretrieve(
    #             url = self.config.source_URL,
    #             filename=self.config.local_data_file
    #         )
    #         logging.info(f"{filename} downloaded! With following info: \n{headers}")
    #     else:
    #         logging.info(f"File already exists of size: {getsize(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)