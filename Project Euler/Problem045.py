# Problem 45: Triangular, pentagonal, and hexagonal
# http://projecteuler.net/problem=45

# we need to find positive integer solutions for the equation
# 0 = t^2 - t - 3p^2 - p

def compare(t, p):
	return (t ** 2 + t) - (3 * p ** 2 - p)

# starting values
t = 286
p = 165

while True:
	result = compare(t, p)

	if result > 0:
		p = p + 1
	elif result < 0:
		t = t + 1
	elif t % 2 == 1:
		print int(0.5 * (t ** 2 + t))
		break
	else:
		p = p + 1
		t = t + 1
