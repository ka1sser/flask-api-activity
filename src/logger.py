"""This module handles the creation of the logger instance and log file creation"""

import logging
import os
from logging.handlers import TimedRotatingFileHandler


def initialize_logger(log_path, log_file_name, logger_type):
    """
    This function will create an instance of a logger.

    Args:
        log_path (str): Directory where to output the log file. This path is indicated in the config file
        log_file_name (str): File name of the log file
        logger_type (str): Name of the logger

    Returns:
        logger (logging.Logger): Returns the instance of the logger created
    """

    os.makedirs(log_path, exist_ok=True)
    log_file = os.path.join(log_path, log_file_name)

    logger = logging.getLogger(logger_type)
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(log_file, when="s", interval=5, backupCount=7)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
