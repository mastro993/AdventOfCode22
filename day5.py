
# https://adventofcode.com/2022/day/5

import re
from functools import reduce

crate_pattern = r"(\s{3}|\[[A-Z]\])\s"
move_pattern = r"move ([0-9]*) from ([0-9]*) to ([0-9]*)"


def clean(x): return x.replace(" ", "").replace("[", "").replace("]", "")


def main():
    f = open("input5.txt", "r")
    lines = f.readlines()

    stacks = [[], [], [], [], [], [], [], [], []]
    moves = []

    # Gettings initial stacks
    while len(lines) > 0:
        line = lines.pop(0)
        crates = [clean(l) for l in re.findall(crate_pattern, line)]

        i = 0
        for crate in crates:
            if crate != "":
                stacks[i].append(crate)
            i += 1

        if line == "\n":
            break

    # Getting moves
    while len(lines) > 0:
        line = lines.pop(0).strip()
        move = tuple(int(item) for item in re.findall(move_pattern, line)[0])
        moves.append(move)

    # Performing moves
    for move in moves:
        size, origin, to = move

        moving = stacks[origin - 1][0: size]
        # moving.reverse() # Uncomment to reverse the order of the crates
        stacks[to - 1][0:0] = moving
        stacks[origin - 1] = stacks[origin - 1][size:len(stacks[origin - 1])]

    result = ''

    for stack in stacks:
        result += stack[0]

    print("Day 5 - top crates: ", result)


if __name__ == "__main__":
    main()
