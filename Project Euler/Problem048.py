# Problem 48: Self powers
# http://projecteuler.net/problem=48

print sum([i ** i for i in range(1, 1001)]) % 10000000000
