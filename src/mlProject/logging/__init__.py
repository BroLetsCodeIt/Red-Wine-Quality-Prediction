import os 
import sys
import logging


# %(asctime)s  -> current time and date 
# %(levelname)s -> At what level it is running like - > if it is in the root folder , it will give root  
# %(module)s -> module name
# %(module)s -> message


logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"


log_dir =  'logs'


log_filepath = os.path.join(log_dir , 'running_log.log')


os.makedirs(log_dir , exist_ok=True)  # exist_ok = True -> means if the folder is not available then only it will create otherwise not.


logging.basicConfig(
    level=logging.INFO , 
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # from this we will print/display/save the log in the running.log file  
        logging.StreamHandler(sys.stdout)  # from this we will print/display the log in the terminal
    ]
)


logger = logging.getLogger("Wine Quality Prediction")