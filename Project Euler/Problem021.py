# http://projecteuler.net/problem=21

# ---------------------
# from Problem 12

def mult(a, b):
	list = []
	for i in a:
		for j in b:
			list.append(i*j)
	return set(sorted(list))

divisors = {}
def div(n):
	if n not in divisors:
		if n < 4:
			divisors[n] = set([1, n])
		else:
			a = int(n ** 0.5)
			while n % a != 0:
				a = a - 1

			if a == 1:
				divisors[n] = set([1, n])
			else:
				divisors[n] = mult(div(n/a), div(a))

	return divisors[n]

 # -----------------------

amicables = {}

d = {}
for i in range(1, 10000):
	d[i] = sum(n for n in div(i)) - i

for i in range(1, 10000):
	if d[i] in d and d[d[i]] == i and d[i] != i:
		amicables[i] = True
		amicables[d[i]] = True

print sum(number for number in amicables)
