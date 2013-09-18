# http://projecteuler.net/problem=29

distinct = {}

for a in range(2, 101):
	for b in range(2, 101):
		distinct[a ** b] = True

print len(distinct.keys())
