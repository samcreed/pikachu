# http://projecteuler.net/problem=28

# spiral can be reduced to formula

k = 3
sum = 1
while k <= 1001:
	sum += (4 * k * k) - 6 * (k - 1)
	k += 2

print sum