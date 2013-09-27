# Problem 52: Permuted multiples

found = False
j = 2
while not found:
	j += 1
	for i in range(10 ** (j - 1), 10 ** j / 6):
		x1 = ''.join(sorted(str(1 * i)))
		x2 = ''.join(sorted(str(2 * i)))
		x3 = ''.join(sorted(str(3 * i)))
		x4 = ''.join(sorted(str(4 * i)))
		x5 = ''.join(sorted(str(5 * i)))
		x6 = ''.join(sorted(str(6 * i)))

		if x1 == x2 == x3 == x4 == x5 == x6:
			print i
			found = True
			break
