# Problem #1
# Multiples of 3 and 5
# START: 2016.01.29


# Method 1 - Brute Force
def main():
    i = 1
    sum = 0
    while i < 1000:
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
        i += 1

    return sum


main()
