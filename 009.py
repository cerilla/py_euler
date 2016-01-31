# Problem 009
# Special Pythagorean triplet


def get_pythagoras_triplet(m, n):
    a = abs(m**2 - n**2)
    b = 2 * m * n
    c = m**2 + n**2
    return [a, b, c]


for n in range(1,25):
    for m in range(n+1, 25):
        a = get_pythagoras_triplet(m, n)
        numsum = a[0] + a[1] + a[2]
        if numsum == 1000:
            nummult = a[0] * a[1] * a[2]
            print(a)
            print(nummult)
            exit()
