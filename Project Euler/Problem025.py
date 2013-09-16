# http://projecteuler.net/problem=25

f = {}
def F(n):
	if n not in f:
		if n < 2:
			f[n] = 1
		else:
			f[n] = F(n - 1) + F(n - 2)
	return f[n]

def digits(n):
	return len(str(n))

n = 10
term = F(n)
while digits(term) < 1000:
	n = n + 1
	term = F(n)

print n + 1
