# http://projecteuler.net/problem=4

# the palindrome can be written as abccba (where a, b, c are whole numbers)
# this simplifies to 11(9091a + 910b + 100c)

max = 0
i = 999
j = 990

while i > 100:
  j = 990
  while j > 100:
     product = i * j
     if product > max:
        productString = str(product)
        # palindrome check
        if (productString == productString[::-1]):
           max = product
     j -= 11
  i -= 1

print max
