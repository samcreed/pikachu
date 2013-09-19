# Problem 33: Digit cancelling fractions
# http://projecteuler.net/problem=33

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def reduce2lct(n, d):
	div = gcd(n, d)
	return n / div, d / div

def cancels(n, d):
	nr, dr = reduce2lct(n, d)

	ncomp = [n / 10, n % 10]
	dcomp = [d / 10, d % 10]

	# don't count trivial examples
	if 0 in ncomp or 0 in dcomp:
		return False

	if ncomp[0] == dcomp[0]:
		n = ncomp[1]
		d = dcomp[1]
	elif ncomp[0] == dcomp[1]:
		n = ncomp[1]
		d = dcomp[0]
	elif ncomp[1] == dcomp[0]:
		n = ncomp[0]
		d = dcomp[1]
	elif ncomp[1] == dcomp[1]:
		n = ncomp[0]
		d = dcomp[0]
	else:
		return False

	n, d = reduce2lct(n, d)

	return nr == n and dr == d

numerprod = 1
denomprod = 1
for numerator in range(10, 100):
	for denominator in range(numerator + 1, 100):
	 	if cancels(numerator, denominator):
	 		numerprod *= numerator
	 		denomprod *= denominator

num, denom = reduce2lct(numerprod, denomprod)
print denom
