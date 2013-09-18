# http://projecteuler.net/problem=30

sum = 0
for i in range(2, 1000000):
	f = (i % 1000000) / 100000
	a = (i % 100000) / 10000
	b = (i % 10000) / 1000
	c = (i % 1000) / 100
	d = (i % 100) / 10
	e = (i % 10)

	if a ** 5 + b ** 5 + c ** 5 + d ** 5 + e ** 5 + f ** 5 == i:
		print i
		sum += i

print sum
