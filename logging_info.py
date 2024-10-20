import logging
import sys
from datetime import datetime


def logging_setup():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_name = "logs"+"\\"+str(datetime.now().strftime("%Y-%m-%d")) + "_" + "date_logs_file"

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",datefmt='%Y-%m-%d %H:%M:%S')

    stream_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(file_name)

    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger

