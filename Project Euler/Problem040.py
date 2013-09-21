# Problem 30: Champernowne's constant
# http://projecteuler.net/problem=40

strs = []
i = 0
while len(strs) < 300000:
	strs.append(str(i))
	i = i + 1

strs = "".join(strs)

print int(strs[1]) * int(strs[10]) * int(strs[100]) * int(strs[1000]) * int(strs[10000]) * int(strs[100000]) * int(strs[1000000])
