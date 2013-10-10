# Problem 86: Cuboid route
# http://projecteuler.net/problem=86

# calculate minimum distance s
def s2(x, y, z):
	return (x ** 2 + (y + z) ** 2)

# check: is (x, y + z, s) a pythagorean triple?
def findTotal(M, squares):
	total = 0
	for y in range(1, M + 1):
		for z in range(1, y + 1):
			s = s2(M, y, z)
			if s in squares:
				total += 1
	return total



power10 = {}
for i in range(100):
	power10[10 ** i] = True

# initial setup
print "calculating squares..."
target = 10000000
squares = {}
for i in range(target):
	if i in power10:
		print i
	squares[i * i] = True

# find upper bound
print "calculating upper bound..."
M = 0
total = 0
while total <= target:
	M = M + 1
	total += findTotal(M, squares)
	print M, total
