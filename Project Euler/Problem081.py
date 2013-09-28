# Problem 81: Path sum: two ways
# http://projecteuler.net/problem=81

M = {}
S = {}

# load data into matrix
with open("matrix.txt") as f:
	r = 0
	for line in f:
		c = 0
		elements = line.split(",")
		for e in elements:
			M[r, c] = int(e)
			c = c + 1
		r = r + 1

# compute local optimal sums
for i in range(r):
	for j in range(c):
		if i == 0 and j == 0:
			S[0, 0] = M[0, 0]
		elif i == 0:
			S[0, j] = S[0, j - 1] + M[0, j]
		elif j == 0:
			S[i, 0] = S[i - 1, 0] + M[i, 0]
		else:
			S[i, j] = min(S[i - 1, j], S[i, j - 1]) + M[i, j]

print S[r - 1, c - 1]
