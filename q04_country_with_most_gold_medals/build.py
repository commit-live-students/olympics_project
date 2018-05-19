# %load q04_country_with_most_gold_medals/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q03_split_country.build import q03_summer_gold_medals


def q04_country_with_most_gold_medals(path):
    'write your solution here'
    df = q03_summer_gold_medals(path)
    
    a=pd.DataFrame(((df[:]['Gold']).values).astype(np.int),index=df['# Summer'].index)
    max_country=(a[2].argmax())
    #print(a[a.index==max_country])
    return str(max_country)


