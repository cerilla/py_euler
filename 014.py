# Problem 014
# Longest Collatz sequence


def collatz_next_sequence(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3 * n + 1


def collatz_chain_num(n):
    counter = 0
    while n != 1:
        n = collatz_next_sequence(n)
        counter += 1
    return counter


maxval = [1, 0]
for i in range(2,1000000):
    print("Now checking {}".format(i))
    val = collatz_chain_num(i)
    if val > maxval[1]:
        maxval = [i, val]

print(maxval)