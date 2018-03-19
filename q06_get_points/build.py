import pandas as pd
from pandas import Series
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q06_get_points(path):

    df = q02_rename_columns(path)
    gold = []
    silver = []
    bronze = []

    for medal in df.Gold.values:
        gold.append(int(medal[0]) + int(medal[1]) + int(medal[2]))

    for medal in df.Silver.values:
        silver.append(int(medal[0]) + int(medal[1]) + int(medal[2]))

    for medal in df.Bronze.values:
        bronze.append(int(medal[0]) + int(medal[1]) + int(medal[2]))

    return ((Series(gold) * 3) + Series(silver) * 2 + Series(bronze) * 1)

q06_get_points("data/olympics.csv")
