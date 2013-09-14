# http://projecteuler.net/problem=22

with open("names.txt") as f:
	data = f.read()

# parse each name and remove quotation marks, then sort
names = sorted([name[1:-1] for name in data.split(",")])

score = 0
for i in range(len(names)):
	sub = 0

	for char in names[i]:
		sub += ord(char) - ord("A") + 1
	score += sub * (i + 1)

print score
