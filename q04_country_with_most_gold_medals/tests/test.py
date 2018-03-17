import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q04_country_with_most_gold_medals
from inspect import getfullargspec
import pandas

path = "data/olympics.csv"
df = q04_country_with_most_gold_medals(path)

class TestRead_csv_data_to_df(TestCase):

	def test_args(self):
		arg = getfullargspec(q04_country_with_most_gold_medals).args
		self.assertEqual(len(arg),1 ,"Expected argument(s) %d, Given %d" % (1,len(arg)) )


	def test_output_type(self):
	    self.assertIs(type(df) ,str, "The Expected return type does not match the return type")
