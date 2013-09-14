# http://projecteuler.net/problem=23

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

abundant = {}
def is_abundant(n):
	return n < (sum(i for i in div(n)) - n)

for i in range(12, 28124):
	if is_abundant(i):
		abundant[i] = True

sumx = sum(xrange(24))
for i in range(25, 28124):
	not_abundant = True
	for a in abundant:
		if a >= i:
			break
		if is_abundant(i - a):
			not_abundant = False # since i = (i - a) + a
			break
	if not_abundant:
		sumx += i

print sumx
