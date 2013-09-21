# Problem 39: Integer right triangles
# http://projecteuler.net/problem=39

squares = {}
for i in range(2000):
	squares[i * i] = True

pcount = [0] * 1000
for a in range(3, 333):
	for b in range(a, 1000):
		c2 = a * a + b * b
		if c2 in squares:
			c = int(c2 ** 0.5)
			if a + b + c < 1000:
				pcount[a + b + c] += 1

maxp = 0
maxi = 0
for i in range(len(pcount)):
	if pcount[i] > maxp:
		maxp = pcount[i]
		maxi = i

print maxi
