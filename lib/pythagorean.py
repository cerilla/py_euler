# pythagorean Library
# Contain code to work with pythagorean numbers


def get_triplet(m, n):
    a = abs(m**2 - n**2)
    b = 2 * m * n
    c = m**2 + n**2
    return [a, b, c]