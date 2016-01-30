# Problem 004
# Largest palindrome product


def is_palindrome(x):
    str_pal = str(x)
    for i in range(int(len(str_pal) / 2)):
        if str_pal[i] != str_pal[-(i + 1)]:
            return False
    return True


i = 100
bigpal = 0

for a in range(i, 1000):
    for b in range(i, 1000):
        val = a * b
        if is_palindrome(val) and val > bigpal:
            bigpal = val

print(bigpal)
