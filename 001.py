# Problem 001
# Multiples of 3 and 5

i = 1
sum = 0
while i < 1000:
    if (i % 3 == 0 or i % 5 == 0):
        sum += i
    i += 1

print(sum)
