# http://projecteuler.net/problem=12

def T(n):
	return (n * (n + 1)) / 2

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


n = 20
divtn = len(div(T(n)))
while divtn < 500:
	n = n + 1
	divtn = len(div(T(n)))

print T(n)
