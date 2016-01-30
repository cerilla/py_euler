from eulerlib import get_sieve, get_smallest_factor


val = 700851475143
sqval = int(val**.5)
sl = get_sieve(sqval, "sieve.txt")
factor = []


while val != 1:
    divider = get_smallest_factor(val, sl)[1]
    factor.append(int(divider))
    val =val/divider

print(factor)