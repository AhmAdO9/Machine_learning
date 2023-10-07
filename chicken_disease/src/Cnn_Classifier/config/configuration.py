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



class ConfigurationManager:
    def __init__(self,
                  config_filepath=CONFIG_FILE_PATH,
                  params_filepath=PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories(self.config.artifacts_root)


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories(config.root_dir)

        data_ingestion_config = DataIngestionConfig(

                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file = config.local_data_file,
                unzip_dir=config.unzip_dir
        )

        return data_ingestion_config



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


try:

    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    # data_ingestion.dowmnload_file()
    data_ingestion.extract_zip_file()
    
except Exception as e:
    raise CustomEx(e, sys)
