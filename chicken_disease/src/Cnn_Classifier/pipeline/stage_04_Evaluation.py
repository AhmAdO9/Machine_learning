from Cnn_Classifier.config.configuration import ConfigurationManager
from Cnn_Classifier.components.prepare_base_model import PrepareBaseModel
from Cnn_Classifier.logger import logging
from  Cnn_Classifier.exception import CustomEx
import sys
from Cnn_Classifier.components.prepare_callbacks import PrepareCallback
from Cnn_Classifier.components.training import Training
from Cnn_Classifier.components.evaluation import Evaluation


class EvaluationPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
