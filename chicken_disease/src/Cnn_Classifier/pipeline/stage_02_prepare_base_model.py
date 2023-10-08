from Cnn_Classifier.config.configuration import ConfigurationManager
from Cnn_Classifier.components.prepare_base_model import PrepareBaseModel
from Cnn_Classifier.logger import logging
from  Cnn_Classifier.exception import CustomEx
import sys

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


