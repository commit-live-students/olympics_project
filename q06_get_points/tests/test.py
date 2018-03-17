import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q06_get_points
from inspect import getfullargspec

import pandas

path = "data/olympics.csv"
df = q06_get_points(path)
values = list(df[:10].values)
check = list([2, 27, 130, 16, 22, 923, 569, 43, 24, 1])


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q06_get_points).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_instance(self):
        self.assertIsInstance(df, pandas.Series, "The Expected return type does not match with the given")

    def test_return(self):
        self.assertListEqual(values, check, "The Expected return does not match the output")
