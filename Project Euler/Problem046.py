# Problem 46: Goldbach's other conjecture
# http://projecteuler.net/problem=46

primes = {}
def is_prime(n):
	if n not in primes:
		for i in range(2, int(n ** 0.5) + 1):
			if n % i == 0:
				return False
		primes[n] = True
	return primes[n]

def check(k, a):
	return is_prime(k - 2 * a ** 2)

k = 4
while True:
	print k
	while k % 2 == 0 or is_prime(k):
		k += 1

	good = True
	for a in range(int((0.5 * k) ** 0.5) + 1):
		if check(k, a):
			good = False
			break

	if not good:
		print k
		break
	else:
		k += 1
