# %load q04_country_with_most_gold_medals/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals
path = './data/olympics.csv'

def q04_country_with_most_gold_medals(path):

    df = q03_summer_gold_medals(path)
    d = df.Gold
    v = d.iloc[:,0].astype(int) + d.iloc[:,1].astype(int) +d.iloc[:,2].astype(int)
    country_with_most_golds = v.nlargest(1).index[0].strip()
    return country_with_most_golds


q04_country_with_most_gold_medals(path)



