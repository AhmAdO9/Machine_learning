from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from logger import logging
from exception import CustomException
import sys

STAGE_NAME = "Data Ingestiotn Stage" 

try: 
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<< \n \n x==============x")
except Exception as e:
    raise CustomException(e, sys)