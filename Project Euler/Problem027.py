# http://projecteuler.net/problem=27

def quadratic(n, a, b):
	return n * n + a * n + b

# Taken from Problem 10
primes = { 2:True, 3:True, 5:True, 7:True }
def compute_primes(n):
	number = 10
	while number < n:
		number += 1
		isprime = True
		for p in primes:
			if p * p > number:
				break
			if number % p == 0:
				isprime = False
				break
		if isprime:
			primes[number] = True


def count_primes(a, b):
	n = 0
	while quadratic(n, a, b) in primes:
		if n > 10:
			print quadratic(n, a, b),
		n = n + 1
	return n

print "computing primes..."
compute_primes(2001000)
maxprimes = 0
maxi = 0
maxj = 0
print "finding max n..."
for i in range(-999, 1000):
	print i
	for j in range(-999, 1000):
		count = count_primes(i, j)
		if count > maxprimes:
			maxi = i
			maxj = j
			maxprimes = count

print maxi * maxj
