import datetime
import os
from date_calc import Retirement

os.system('clear')

print ("Hello World!")

mydob = datetime.date(1967, 6, 2)
now = datetime.date.today()

lifeline = Retirement(mydob, now)
print "Date of birth - %s, date now - %s" % (lifeline.dob.strftime("%d-%m-%Y"), lifeline.progress.strftime("%d-%m-%Y"))
print "%s days have passed since you were born" % lifeline.lifetime
print "Optimisticly you will retire %d days (%s months, %s years and %s months) from now on %s" % (lifeline.optimistic_days, lifeline.optimistic_months, lifeline.optimistic_years, (lifeline.optimistic_months - (lifeline.optimistic_years * 12)), lifeline.optimistic.strftime("%d-%m-%Y"))
print "Pragmaticly you will retire %d days (%s months, %s years and %s months) from now on %s" % (lifeline.pragmatic_days, lifeline.pragmatic_months, lifeline.pragmatic_years, (lifeline.pragmatic_months - (lifeline.pragmatic_years * 12)), lifeline.pragmatic.strftime("%d-%m-%Y"))
print "Pessimisticly you will retire %d days (%s months, %s years and %s months) from now on %s" % (lifeline.pessimistic_days, lifeline.pessimistic_months, lifeline.pessimistic_years, (lifeline.pessimistic_months - (lifeline.pessimistic_years * 12)), lifeline.pessimistic.strftime("%d-%m-%Y"))
print "Optimistic Percent ", format(lifeline.optimistic_percent, ".3f")
print "Pragmatic Percent ", format(lifeline.pragmatic_percent, ".3f")
print "Pessimistic Percent ", format(lifeline.pessimistic_percent, ".3f")
print ""