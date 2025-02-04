"""This module is used for handling the csv files"""
import os
import pandas as pd
import config

config_file = config.import_config()
db = config.import_database_path(config_file)

def read_csv():
    """
    This method reads the csv file from teh directory

    Returns:
        database (pandas.DataFrame): Returns the dataframe from the csv file
    """
    if not os.path.exists(db):
        return "File does not exist."
    
    database = pd.read_csv(db)
    
    return database
