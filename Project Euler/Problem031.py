# Coin Sums
# http://projecteuler.net/problem=31

N = {}

def g(a, b):
	return N[a] * (N[b] + (1 - N[a]) / 2)

N[1] = 1
N[2] = 1 + g(1, 1)
N[4] = g(2, 2)
N[5] = 1 + g(1, 4)
N[10] = 1 + g(5, 5)
N[20] = 1 + g(10, 10)
N[40] = g(20, 20)
N[50] = 1 + g(10, 40)
N[100] = 1 + g(50, 50)
N[200] = 1 + g(100, 100)

print N[200]