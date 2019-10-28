import datetime
from dateutil.relativedelta import relativedelta

define_optimistic = 55
define_pragmatic = 60
define_pessimistic = 65

class Retirement:
	def __init__ (self, dob, progress):
		self.dob = dob
		self.progress = progress

	@property
	def lifetime(self):
		return abs((self.progress - self.dob).days)

	@property
	def optimistic(self):
		return self.dob + relativedelta(years=+define_optimistic)

	@property
	def optimistic_days(self):
		return abs((self.dob + relativedelta(years=+define_optimistic) - self.progress).days)

	@property
	def optimistic_months(self):
		target_date = self.dob + relativedelta(years=+define_optimistic)
		months = (target_date.year - self.progress.year) * 12 + (target_date.month - self.progress.month)
		return months

	@property
	def optimistic_years(self):
		target_date = self.dob + relativedelta(years=+define_optimistic)
		years = (target_date.year - self.progress.year - 1)
		return years

	@property
	def pragmatic(self):
		return self.dob + relativedelta(years=+define_pragmatic)

	@property
	def pragmatic_days(self):
		return abs((self.dob + relativedelta(years=+define_pragmatic) - self.progress).days)


	@property
	def pragmatic_months(self):
		target_date = self.dob + relativedelta(years=+define_pragmatic)
		months = (target_date.year - self.progress.year) * 12 + (target_date.month - self.progress.month)
		return months	

	@property
	def pragmatic_years(self):
		target_date = self.dob + relativedelta(years=+define_pragmatic)
		years = (target_date.year - self.progress.year -1)
		return years

	@property
	def pessimistic(self):
		return self.dob + relativedelta(years=+define_pessimistic)

	@property
	def pessimistic_days(self):
		return abs((self.dob + relativedelta(years=+define_pessimistic) - self.progress).days)

	@property
	def pessimistic_months(self):
		target_date = self.dob + relativedelta(years=+define_pessimistic)
		months = (target_date.year - self.progress.year) * 12 + (target_date.month - self.progress.month)
		return months	

	@property
	def pessimistic_years(self):
		target_date = self.dob + relativedelta(years=+define_pessimistic)
		years = (target_date.year - self.progress.year -1)
		return years

	@property
	def optimistic_percent(self):
		return float((self.dob + relativedelta(years=+define_optimistic) - self.progress).days) / float((self.lifetime + (self.dob + relativedelta(years=+define_optimistic) - self.progress).days)) * 100


	@property
	def pragmatic_percent(self):
		return float((self.dob + relativedelta(years=+define_pragmatic) - self.progress).days) / float((self.lifetime + (self.dob + relativedelta(years=+define_pragmatic) - self.progress).days)) * 100

	@property
	def pessimistic_percent(self):
		return float((self.dob + relativedelta(years=+define_pessimistic) - self.progress).days) / float((self.lifetime + (self.dob + relativedelta(years=+define_pessimistic) - self.progress).days)) * 100		
