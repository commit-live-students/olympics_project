import pandas as pd
import numpy as np

path = './data/olympics.csv'
def q01_load_data(path):
    df= pd.read_csv(path, header =0)
    new_header = df.iloc[0]
    new_header[0] = 'country name'
    df = df[1:]  
    df.columns = new_header  
    return df
    
q01_load_data(path)

