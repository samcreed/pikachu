# Problem 38: Pandigital multiples
# http://projecteuler.net/problem=38

def is_pandigital(n):
	n = str(n)
	digits = [str(d) for d in range(1, 10)]
	for d in digits:
		if d not in n:
			return False
	return len(n) == 9

max = 0
for i in range(123, 321):
	candidate = int(str(i) + str(i * 2) + str(i * 3))
	if is_pandigital(candidate) and candidate > max:
		max = candidate

for i in range(5123, 9876):
	candidate = int(str(i) + str(i * 2))
	if is_pandigital(candidate) and candidate > max:
		max = candidate

print max
