
for c in range(1000):
	for b in range(c):
		for a in range(b):
			if a + b + c == 1000 and a*a + b*b == c*c:
				print a*b*c
				break
