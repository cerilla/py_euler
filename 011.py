# Problem 011
# Largest product in a grid

from eulerlib import mult_list_content

# Get text list to work at
with open("etc/011_dump.txt") as f:
    dump = [line.rstrip('\n').split(' ') for line in f]

