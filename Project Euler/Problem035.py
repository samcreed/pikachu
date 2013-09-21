
import itertools

def compute_primes(limit):
	a = [True] * limit
	a[0] = a[1] = False

	for (i, isprime) in enumerate(a):
		if isprime:
			for n in range(i*i, limit, i):
				a[n] = False
	return a

def perms(n):
	return [int("".join(p)) for p in itertools.permutations(n)]

def is_prime(n):
	for i in range(2, int((n ** 0.5) + 1)):
		if n % i == 0:
			return False
	return True

def circular_prime(n, primes):
	ps = perms(str(n))
	for perm in ps:
		if not primes[perm]:
			if not is_prime(perm):
				print perm
				return False
			else:
				print "\t", perm
	return True

primes = compute_primes(2000000)
count = 0
for i in range(2, 1000000):
	if primes[i] and circular_prime(i, primes):
		print i
		count += 1

print count
