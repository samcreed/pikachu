# Problem 99: Largest exponential
# http://projecteuler.net/problem=99

# store a and b as the maximum value a^b
a = 1
b = 1
ln = 0
maxln = 0

with open("base_exp.txt") as f:
	for line in f:
		ln = ln + 1
		c, d = [int(x) for x in line.split(",")]
		
		# we want to check if a^b > c^d
		# an equivalent check is a^(b/d) > c
		x = b * 1.0 / d

		if c > a ** x:
			a = c
			b = d
			maxln = ln

print maxln
