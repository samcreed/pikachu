# Problem 36: Double-base palindromes

def is_palindrome(n):
	return n == n[::-1]

sum = 0

for i in range(1000000):
	if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
		sum += i

print sum