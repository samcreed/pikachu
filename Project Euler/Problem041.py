# Problem 41: Pandigital prime
# http://projecteuler.net/problem=41

import itertools

def is_prime(n):
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

found = False
startperm = "87654321"
while not found:
	for pandigital in itertools.permutations(startperm):
		pandigital = int("".join(pandigital))
		if is_prime(pandigital):
			print pandigital
			found = True
			break
	startperm = startperm[1:]
