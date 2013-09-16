# http://projecteuler.net/problem=24

def fact(n):
	if n < 3:
		return n
	else:
		return n * fact(n - 1)

def find_term(target, count, available):
	terms = fact(len(available) - 1)
	x = 0
	for num in available:
		if count + terms < target:
			count += terms
		elif count + terms >= target:
			print num,
			return find_term(target, count, available - set([num]))

find_term(1000000, 0, set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print 0
