# http://projecteuler.net/problem=67

triangle = []

# read in the triangle, and format
f = open("triangle2.txt", "r")
for line in f:
    row = [int(num) for num in line.strip().split(" ")]
    triangle.append(row)

#print triangle

# find max path sum with dynamic programming approach, bottom-up
for i in range(len(triangle) - 2, -1, -1):
    for j in range(i + 1):

        # add max of lower two terms to determine local optimal path
        triangle[i][j] = triangle[i][j] + max(triangle[i + 1][j], triangle[i + 1][j + 1])

print triangle[0][0]
