# http://projecteuler.net/problem=2

sum = 0
t1 = 1
t2 = 1

while t1 < 4000000:
    if t1 % 2 == 0:
        sum += t1

    # calculate next Fibonacci numbers iteratively
    temp = t1
    t1 = t1 + t2
    t2 = temp

print sum
