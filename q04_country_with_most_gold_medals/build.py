import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals


def q04_country_with_most_gold_medals(path):
    df = q03_summer_gold_medals(path)
    dfnew = df['Gold']
    total_column = (dfnew.iloc[:,2:3])
    top_max = total_column.loc[df['Gold'].idxmax()]
    top =(top_max).index[0].replace("\xc2\xa0", "")
    return top
