# Problem 010
# Summation of primes

from eulerlib import get_sieve

minval = 1000000
sum = 0
sl = get_sieve(minval, "sieve.txt")

for x in sl:
    if x >= minval:
        print(sum)
        return 0
    else:
        sum += x

print(sum)
