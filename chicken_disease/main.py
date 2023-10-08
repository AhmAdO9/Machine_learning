from Cnn_Classifier.logger import logging
from Cnn_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Cnn_Classifier.exception import CustomEx
import sys
from Cnn_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Cnn_Classifier.pipeline.stage_03_training import TrainingPipeline

STAGE_NAME = "Data Ingestion stage"
if __name__=="__main__":
    try:
        logging.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logging.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<< \n\nx=============x")
    except Exception as e:
        raise CustomEx(e, sys)
    

STAGE_NAME = "Prepare base model"
if __name__=="__main__":
    try:
        logging.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<< \n\nx=============x")
    except Exception as e:
        raise CustomEx(e, sys)
    

STAGE_NAME = "training"
if __name__=="__main__":
    try:
        logging.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<< \n\nx=============x")
    
    except Exception as e:
        raise CustomEx(e, sys)