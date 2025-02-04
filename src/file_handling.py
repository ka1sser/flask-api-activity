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
        return pd.DataFrame()

    database = pd.read_csv(db)

    return database


def write_csv(df):
    """
    This function overwrites the existing csv file

    Args:
        df (pandas.DataFrame): New dataframe created after updating the old one
    """
    df.to_csv(db, index=False)
