import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

path="./data/olympics.csv"
def q06_get_points(path):
    "write your solution here"
    df = q02_rename_columns(path="./data/olympics.csv")
    pt_g = df['Gold'].astype(int)*3
    pt_s = df['Silver'].astype(int)*2
    pt_b = df['Bronze'].astype(int)*1
    gold_pts = pt_g.iloc[:,0] +pt_g.iloc[:,1]+pt_g.iloc[:,2]
    silver_pts = pt_s.iloc[:,0] +pt_s.iloc[:,1]+pt_s.iloc[:,2]
    bronze_pts = pt_b.iloc[:,0] +pt_b.iloc[:,1]+pt_b.iloc[:,2]
    Points = gold_pts + silver_pts + bronze_pts
    return Points
