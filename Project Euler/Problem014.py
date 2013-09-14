# http://projecteuler.net/problem=14

clen = {}
def collatz(n):
	if not n in clen:
		if n < 3:
			clen[n] = n
		elif n % 2 == 0:
			clen[n] = 1 + collatz(n / 2)
		else:
			clen[n] = 1 + collatz(3 * n + 1)
	return clen[n]

maxc = 0
maxi = 0
for i in range(1000000):
	c = collatz(i)
	if c > maxc:
		maxc = c 
		maxi = i

print maxi
