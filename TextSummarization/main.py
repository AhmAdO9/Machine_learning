from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
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



STAGE_NAME = "Data Validation" 

try: 
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<< \n \n x==============x")
except Exception as e:
    raise CustomException(e, sys)



STAGE_NAME = "Data Transformation" 

try: 
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<< \n \n x==============x")
except Exception as e:
    raise CustomException(e, sys)



STAGE_NAME = "Model Trainer" 

try: 
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<< \n \n x==============x")
except Exception as e:
    raise CustomException(e, sys)