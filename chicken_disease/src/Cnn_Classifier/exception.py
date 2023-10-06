import sys
from src.logger import logging


def get_error_details(error, error_details:sys):
    _,_,exc_tb= error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line = exc_tb.tb_lineno
    error_message = f"Exception in python script {0}, line {1}, error_message: {2}".format(filename, line, str(error))

    logging.info(error_message)
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_details:sys):
        self.error_message = get_error_details(error, error_details)

    
    def __str__(self):
        return self.error_message