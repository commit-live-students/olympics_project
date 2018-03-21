import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path = "data/olympics.csv"
def q06_get_points(path):
    df = q02_rename_columns(path)
    gold_points =  df['Gold'].iloc[:-1,2].astype(int)*3
    silver_points =  df['Silver'].iloc[:-1,2].astype(int)*2
    bronze_points =  df['Bronze'].iloc[:-1,2].astype(int)*1
    total_points = gold_points + silver_points + bronze_points
    df['Points'] = total_points
    return total_points

#print(q06_get_points(path))
