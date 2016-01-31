# Problem 011
# Largest product in a grid

from eulerlib import mult_list_content

n = 4   # Number of element checked

# Get text list to work at
with open("etc/011_dump.txt") as f:
    dump = [line.rstrip('\n').split(' ') for line in f]

# Convert string to integer

numdump = []
for x in dump:
    numrow = []
    for y in x:
        numrow.append(int(y))
    numdump.append(numrow)

# Get Grid Size

dx = len(numdump[0])
dy = len(numdump)

# Check horizontally

max = 0

for y in range(dy):
    for x in range(dx - n + 1):
        val = 1
        for step in range(n):
            val *= numdump[x + step][y]
        if val > max:
            max = val

# Check vertically

for y in range(dy - n + 1):
    for x in range(dx):
        val = 1
        for step in range(n):
            val *= numdump[x][y + step]
        if val > max:
            max = val

# Check diagonally to bottom right

for y in range(dy - n + 1):
    for x in range(dx - n + 1):
        val = 1
        for step in range(n):
            val *= numdump[x + step][y + step]
        if val > max:
            max = val

# Check diagonally to top right

for y in range(n - 1, dy):
    for x in range(dx - n + 1):
        val = 1
        for step in range(n):
            val *= numdump[x + step][y - step]
        if val > max:
            max = val

print(max)
