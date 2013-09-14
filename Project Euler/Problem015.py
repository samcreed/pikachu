# http://projecteuler.net/problem=15
# Lattice paths problem; solution is binary coeffient 2n choose n for n x n lattice

v = {}
def nCk(n, k):
	if (n, k) not in v:
		if n <= k:
			v[(n, k)] = 1
		elif n == 0 or k == 0:
			v[(n, k)] = 1
		else:
			v[(n, k)] = nCk(n-1, k-1) + nCk(n-1, k)
	return v[(n, k)]

print nCk(40, 20)
