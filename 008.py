# Problem 008
# Largest product in a series

n = 13   # Digit range to be calculated


def mult_list_content(nl):
    total = 1
    for i in nl:
        total *= i
    return total


# Get text string to work at
dump = ""
with open("etc/008_dump.txt", 'r') as f:
    for i in f.readlines():
        dump = dump + str(i).strip('\n')

# Populate list
nl = []
for x in range(n):
    nl.append(int(dump[x]))

total = mult_list_content(nl)

# Iterate along the dump text to calculate
counter = 0

for i in range(n, len(dump) + 1 - n):
    # Calculate and update if result is bigger that current
    nl[counter] = int(dump[i])
    if mult_list_content(nl) > total:
        total = mult_list_content(nl)
    # Check for digit position in list
    counter += 1
    if counter == n:
        counter = 0

print(total)