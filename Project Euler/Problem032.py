# Problem 32: Pandigital products
# http://projecteuler.net/problem=32

sum = 0
pandigital = {}

def f(a, b, c):
	s = str(a) + str(b) + str(c)
	return "0" not in s and "1" in s and "2" in s and "3" in s and "4" in s and "5" in s and "6" in s and "7" in s and "8" in s and "9" in s and len(s) == 9

for a in range(123, 9876):
	for b in range(2, 99):
		c = a * b
		if len(str(c)) < 6 and c not in pandigital:
			if f(a, b, c):
				print a, b, c
				pandigital[c] = True
				sum += c

print sum
