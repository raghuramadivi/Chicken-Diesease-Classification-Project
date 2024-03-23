import os
from pathlib import Path
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


import sys

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) #Using streamHandler u can print log in the terminal.
    ]
)


logger = logging.getLogger("cnnClassifierLogger")