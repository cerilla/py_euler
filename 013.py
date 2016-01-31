# Problem 013
# Large sum

# Get text string to work at
valsum = 0
with open("etc/013_dump.txt", 'r') as f:
    for i in f.readlines():
        valsum += int(i)

print(str(valsum)[-10:])
