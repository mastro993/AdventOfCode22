
# https://adventofcode.com/2022/day/5

import re

crate_pattern = r"(\s{3}|\[[A-Z]\])\s"
move_pattern = r"move ([0-9]*) from ([0-9]*) to ([0-9]*)"


def clean(x): return x.replace(" ", "").replace("[", "").replace("]", "")


f = open("input05.txt", "r")
lines = f.readlines()

stacks = [[], [], [], [], [], [], [], [], []]
moves = []

# Gettings initial stacks
while len(lines) > 0:
    line = lines.pop(0)
    crates = [clean(l) for l in re.findall(crate_pattern, line)]

    for index, crate in enumerate(crates):
        if crate != "":
            stacks[index].append(crate)

    if line == "\n":
        break

# Getting moves
while len(lines) > 0:
    line = lines.pop(0).strip()
    move = tuple(int(item) for item in re.findall(move_pattern, line)[0])
    moves.append(move)

# Performing moves
for size, origin, destination in moves:
    moving = stacks[origin - 1][0: size]
    moving.reverse()
    stacks[destination - 1][0:0] = moving
    stacks[origin - 1] = stacks[origin - 1][size:len(stacks[origin - 1])]

result = ''.join([s[0] for s in stacks])

print("Day 5 - top crates: ", result)
