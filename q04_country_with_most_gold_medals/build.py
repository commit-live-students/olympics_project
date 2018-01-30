import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals


def q04_country_with_most_gold_medals(path):
    df = q03_summer_gold_medals(path)

    #initial goupby for extarcting gold medal columns
    df1 = df.groupby(['country name'])['Gold'].sum()

    #second groupby for adding the gold medal as per country
    df2 = df1.groupby(['country name']).sum()
    return df2.idxmax()
