from Cnn_Classifier.config.configuration import ConfigurationManager
from Cnn_Classifier.components.prepare_base_model import PrepareBaseModel
from Cnn_Classifier.logger import logging
from  Cnn_Classifier.exception import CustomEx
import sys
from Cnn_Classifier.components.prepare_callbacks import PrepareCallback
from Cnn_Classifier.components.training import Training


class TrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )