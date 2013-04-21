# http://projecteuler.net/problem=29

# brute force solution
list = []

for a in range(2, 101):
    for b in range(2, 101):
        list.append(a ** b)

# print the length of the unique values
print len(set(list))
