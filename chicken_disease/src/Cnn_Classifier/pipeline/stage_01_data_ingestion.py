from Cnn_Classifier.config.configuration import ConfigurationManager
from Cnn_Classifier.components.data_ingestion import DataIngestion
from Cnn_Classifier.logger import logging
from  Cnn_Classifier.exception import CustomEx
import sys


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
    
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    

