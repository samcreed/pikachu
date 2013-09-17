# http://projecteuler.net/problem=27

def quadratic(n, a, b):
	return n * n + a * n + b

# Taken from Problem 10
primes = [2, 3, 5, 7]
def compute_primes(n):
	number = 9
	while number < n:
		number += 2
		isprime = True
		for p in primes:
			if p * p > number:
				break
			if number % p == 0:
				isprime = False
				break
		if isprime:
			primes.append(number)


def is_prime(n):
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

def count_primes(a, b, primes_dict):
	n = 0
	while quadratic(n, a, b) in primes_dict:
		n = n + 1
	return n

print "computing primes..."
compute_primes(2001000)
primes_dict = dict(zip(primes, primes))

maxprimes = 0
maxi = 0
maxj = 0
print "finding max n..."
for i in range(-999, 1000):
	for j in range(1, 1000):

		count = count_primes(i, j, primes_dict)
		if count > maxprimes:
			maxi = i
			maxj = j
			maxprimes = count

print maxi * maxj
