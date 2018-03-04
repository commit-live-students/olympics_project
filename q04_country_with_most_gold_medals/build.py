import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals


def q04_country_with_most_gold_medals(path):
    "write your solution here"
    df = q03_summer_gold_medals(path)

    df['Max_Gold']= pd.DataFrame(df.iloc[:,1].astype('int64')) + pd.DataFrame(df.iloc[:,6].astype('int64')) + pd.DataFrame(df.iloc[:,11].astype('int64'))

    return df['Max_Gold'].idxmax()
