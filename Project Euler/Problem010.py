# http://projecteuler.net/problem=10

# find the sum of all primes below 2 million.

primes = [2, 3, 5, 7]

number = 10
sum = sum(primes)

while number < 2000000:
	number += 1
	isprime = True
	for p in primes:
		if p * p > number:
			break
		if number % p == 0:
			isprime = False
			break
	if isprime:
		sum += number
		primes.append(number)

print sum
