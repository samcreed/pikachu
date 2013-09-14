# http://projecteuler.net/problem=19

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def is_leap(year):
	if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
		return 1
	else:
		return 0

days = {}
days["Jan"] = 31
days["Feb"] = 28
days["Mar"] = 31
days["Apr"] = 30
days["May"] = 31
days["Jun"] = 30
days["Jul"] = 31
days["Aug"] = 31
days["Sep"] = 30
days["Oct"] = 31
days["Nov"] = 30
days["Dec"] = 31

sundays = 0
day = 1

for year in range(1901, 2001):
	for month in months:
		if day == 0:
			print month, year
			sundays += 1

		if month == "Feb":
			day = (day + days[month] - 1 + is_leap(year)) % 7
		else:
			day = (day + days[month] - 1) % 7

print sundays
