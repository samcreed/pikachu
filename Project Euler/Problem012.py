# http://projecteuler.net/problem=12

def T(n):
	return n*(n+1)/2

div = {}
def divisors(n):
	if n not in div:
		d = 0
		for i in range(1, n+1):
			if n % i == 0:
				d += 1
		div[n] = d

	return div[n]

# determine upper limit
lower = 0
upper = 10
divtn = 0
print "upper limit"
while divtn <= 500:
	lower = upper
	upper = 2 * upper
	divtn = divisors(T(upper))
	print upper, divtn

# determine lowest n such that divtn > 500
print "narrow"
while upper - lower > 2:
	n = (lower + upper) / 2
	divtn = divisors(T(n))
	print divtn

	if divtn > 500:
		upper = n
	else:
		lower = n

print "done"
