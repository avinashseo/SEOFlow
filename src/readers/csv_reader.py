import pandas as pd

class CSVReader:

    """
        Reads CSV files into pandas DataFrames.
    """
    def __init__(self, path):
        self.path = path

    def read(self): 
        return pd.read_csv(self.path)