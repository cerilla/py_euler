# Problem 006
# Sum square difference

n = 100
square_sum = 0
sum_square = 0

for i in range(n + 1):
    sum_square += i**2
    square_sum += i

square_sum = square_sum ** 2
print(square_sum - sum_square)
