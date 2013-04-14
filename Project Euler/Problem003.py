# http://projecteuler.net/problem=3

number = 600851475143
largest = 1
divisor = 2

# continue until number has been reduced to 1 
while number > 1:
    # find largest prime factor. We don't need to check if the divisor
    # is prime because if its not, the remaining number will not be
    # divisble by it (since we will have already divided out its smaller factors)
    while number % divisor == 0:
        largest = divisor
        number /= divisor

    # could be done smarter by pre-computing primes, but this is space effcient
    divisor += 1

print largest
