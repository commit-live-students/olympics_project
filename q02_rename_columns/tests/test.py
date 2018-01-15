import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q02_rename_columns
from inspect import getargspec
import pandas
import numpy
from numpy.testing import assert_array_equal

path = "data/olympics.csv"
df = q02_rename_columns(path)
columns = list(df.columns.values)
check = ['country name', '# Summer', 'Gold', 'Silver', 'Bronze', 'Total', '# Winter', 'Gold', 'Silver', 'Bronze',
         'Total', '# Games', 'Gold', 'Silver', 'Bronze', 'Combined total']


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getargspec(q02_rename_columns).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_instance(self):
        self.assertIsInstance(df, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_return(self):
        self.assertListEqual(columns,check, "The Expected return does not match with the given return")
