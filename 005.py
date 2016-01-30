# Problem 005
# Smallest number divisible by number 1 to n

import eulerlib

n = 20
pl = eulerlib.get_sieve(20, "sieve.txt")
mult = 1

fl = []     # Factor list
fo = []     # Factor occurence

for a in range(2, n + 1):
    nf = eulerlib.get_all_factor(a, pl)
    print("{}: {}".format(a, nf))
    for f in nf:
        if f not in fl:
            fl.append(f)
            fo.append(1)
        elif nf.count(f) > fo[fl.index(f)]:
            fo[fl.index(f)] = nf.count(f)


print(fl)
print(fo)


for i in range(len(fl)):
    mf = fl[i] ** fo[i]
    print("Multiply by {}".format(mf))
    mult *= mf

print(mult)
