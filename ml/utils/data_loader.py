import pandas as pd
import os

def load_raw_data():
    file_path = os.path.join("data", "raw", "UNSW_NB15_training-set.csv")
    return pd.read_csv(file_path)

