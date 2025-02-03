"""This module is used to load the config files and the parameters in it"""

import tomli


def import_config():
    """
    This function will import the config file to the script.

    Returns:
        config (dict): Returns the config file containing the parameters for the script
    """

    with open(
        "C:/Users/eserkai/OneDrive - Ericsson/Documents/Programming/Python/Training/flask-api-activity/config/config.toml",
        "rb",
    ) as file:
        config = tomli.load(file)

    return config


def import_input_path(config):
    """
    This function will import the "input_path" in "directories" in the config file

    Args:
        config (dict): Config file used for the parameters

    Returns:
        input_path (str): Input path to get the CSV file
    """

    input_path = config["directories"]["input_path"]

    return input_path


def import_log_path(config):
    """
    This function will import the "log_path" in "directories" in the config file

    Args:
        config (dict): Config file used for the parameters

    Returns:
        log_path (str): Log path for the output logs
    """

    log_path = config["directories"]["log_path"]

    return log_path
