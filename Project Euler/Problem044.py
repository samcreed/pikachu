# Problem 44: Pentagon numbers
# http://projecteuler.net/problem=44

p = {}
pv = {}
def pentagon(n):
	if n not in p:
		p[n] = n * (3 * n - 1) / 2
		pv[p[n]] = True
	return p[n]

def is_pentagon(x):
	if x in pv:
		return True
	else:
		res = (24 * x + 1) ** 0.5
		return int(res) == float(res) and int(res) % 6 == 5


i = 5
min = 99999999999999999
zzzz = True
while zzzz:
	i = i + 1
	for j in range(1, i):
		pi = pentagon(i)
		pj = pentagon(j)
		S = pi + pj
		D = pi - pj
		if is_pentagon(S) and is_pentagon(D):
			if D < min:
				min = D
				print min
				zzzz = False

