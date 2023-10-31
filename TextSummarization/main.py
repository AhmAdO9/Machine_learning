from exception import CustomException
import sys
<<<<<<< HEAD
from logger import logging
=======

>>>>>>> d6c8ec6eb314978b44e6798bbd49de35a6b52581

try:
    x = 1/0

except Exception as e:
<<<<<<< HEAD
    logging.info("raised an exception")
=======
>>>>>>> d6c8ec6eb314978b44e6798bbd49de35a6b52581
    raise CustomException(e, sys)
    