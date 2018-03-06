import unittest
import datetime
from date_calc import Retirement

class TestBetween(unittest.TestCase):

	def test_days(self):
		days = Retirement(datetime.date(1967, 6, 2), datetime.date(1968, 6, 2))

		self.assertEqual(days.lifetime, 366)
		
	def test_optimisitc(self):
		optimistic = Retirement(datetime.date(1967, 6, 2), datetime.date(2019, 6, 2))

		self.assertEqual(str(optimistic.optimistic), '2022-06-02')
		self.assertEqual(optimistic.optimistic_days, 1096)

	def test_pragmatic(self):
		pragmatic = Retirement(datetime.date(1967, 6, 2), datetime.date(2019, 6, 2))

		self.assertEqual(str(pragmatic.pragmatic), '2027-06-02')
		self.assertEqual(pragmatic.pragmatic_days, 2922)

	def test_pessimistic(self):
		pessimistic = Retirement(datetime.date(1967, 6, 2), datetime.date(2019, 6, 2))

		self.assertEqual(str(pessimistic.pessimistic), '2032-06-02')
		self.assertEqual(pessimistic.pessimistic_days, 4749)
