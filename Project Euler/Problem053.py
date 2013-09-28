# Problem 53: Combinatoric selections
# http://projecteuler.net/problem=53

f = {0 : 1, 1 : 1}
def fact(n):
	if n not in f:
		f[n] = fact(n - 1) * n
	return f[n]

def check(n, k):
	return fact(n) > 10 ** 6 * fact(k) * fact(n - k)

total = 0
for n in range(10, 101):
	for k in range(1, n):
		if check(n, k):
			total += n - 2 * k + 1
			break

print total
