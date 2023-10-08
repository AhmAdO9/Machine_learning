from Cnn_Classifier.config.configuration import ConfigurationManager
from Cnn_Classifier.components.prepare_base_model import PrepareBaseModel
from Cnn_Classifier.logger import logging
from  Cnn_Classifier.exception import CustomEx
import sys


STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipiline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


# if __name__=="__main__":
#     try:
#         logging.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<")
#         obj = PrepareBaseModelTrainingPipiline()
#         obj.main()
#         logging.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<< \n\nx=============x")
#     except Exception as e:
#         raise CustomEx(e, sys)
    
