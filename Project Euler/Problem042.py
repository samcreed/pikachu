# Problem 42: Coded triangle numbers
# http://projecteuler.net/problem=42

tri = {}
def compute_triangles(n):
	for i in range(1, n):
		tri[i * (i + 1) / 2] = True

def score(word):
	_score = 0
	for letter in word:
		_score += ord(letter) - ord('A') + 1
	return _score


compute_triangles(100)

f = open("words.txt")
words = f.readlines()[0].replace('"', "").split(",")
f.close()

count = 0
for word in words:
	if score(word) in tri:
		count += 1

print count
