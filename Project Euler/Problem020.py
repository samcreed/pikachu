# http://projecteuler.net/problem=20

def fact(n):
	prod = n
	for i in range(1, n):
		prod *= i
	return prod
	
print sum(int(i) for i in str(fact(100)))