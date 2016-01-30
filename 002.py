# Problem 002
# Sum of Even Fibonacci Number

a = 1
b = 2
sum = 2

while b < 4e6:
    c = a + b
    a = b
    b = c
    if b % 2 == 0:
        sum += b

print(sum)
