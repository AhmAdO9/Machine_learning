import logging, os, sys
from datetime import datetime


log_file = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), 'logs', log_file)

os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, log_file)

logging.basicConfig( 
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
    handlers=[
        
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

# logger = logging.getLogger()
