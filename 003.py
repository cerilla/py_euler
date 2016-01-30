# Problem 003
# Largest prime factor

from eulerlib import get_sieve, get_all_factor

val = 13195
sqval = int(val**.5)
sl = get_sieve(sqval, "sieve.txt")

print(max(get_all_factor(val, sl)))
