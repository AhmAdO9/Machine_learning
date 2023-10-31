from exception import CustomException
import sys
from logger import logging

try:
    x = 1/0

except Exception as e:
    logging.info("raised an exception")
    raise CustomException(e, sys)
    