def factorial(n):
	if n <= 2:
		return max(1, n)
	else:
		return factorial(n - 1) * n

def factorial_digits(n):
	return n - sum(factorial(int(i)) for i in str(n))

total = 0
n = 10
while True:
	x = factorial_digits(n)
	if x == 0:
		total += n
		print n, total
	n = n + 1