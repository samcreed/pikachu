# Problem 85: Counting rectangles
# http://projecteuler.net/problem=85

# define Nth Triangle number
def T(n):
	return (n * (n + 1)) / 2

# count for N x M rectangle
def R(n, m):
	return T(n) * T(m)


target = 2000000

min = 0
ans = 0
for n in range(100):
	for m in range(100):
		r = R(n, m)
		if abs(r - target) < abs(min - target):
			min = r
			ans = n * m

print ans
