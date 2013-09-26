# Problem 50: Consecutive prime sum
# http://projecteuler.net/problem=50

def generate_primes(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []
    primesd = {}

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)
        primesd[i] = True

    return primes, primesd


primes, primesd = generate_primes(1000000)
mcount = 0
sum = 0

limit = len(primes)
for i in range(limit):
	seq = []
	sum = 0
	old = mcount

	for j in range(i, limit):
		pj = primes[j]
		seq.append(pj)
		sum += pj

		if sum > primes[-1]:
			break
		if sum in primesd and len(seq) > mcount:
			mcount = len(seq)
			msum = sum
			print mcount, msum

		j += 1

print "final", msum
