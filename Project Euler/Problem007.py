# http://projecteuler.net/problem=7

# initial
primes = [2, 3, 5, 7]

pcount = 4
number = 10

while pcount < 10001:
	number += 1
	isprime = True
	for p in primes:
		if p*p > number:
			break
		if number % p == 0:
			isprime = False
			break
	if isprime:
		pcount += 1
		primes.append(number)

print primes[10001 - 1]
