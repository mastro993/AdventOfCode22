# https://adventofcode.com/2022/day/7


import re

command_pattern = r"^\$ (cd|ls)[ ]?([a-zA-Z0-9/.]*)?"
file_pattern = r"^([0-9]*) ([a-zA-Z]*)([.][a-z]*)?"

max_size = 100000
root = ()


f = open("input07.txt", "r")
lines = [l.rstrip() for l in f.readlines()]

cwd = root
fs = {}

for line in lines:
    if re.match(command_pattern, line):
        cmd, argument = re.findall(command_pattern, line)[0]

        if cmd != "cd":
            continue

        match argument:
            case "..":
                cwd = cwd[:-1]
            case "/":
                cwd = root
            case _:
                cwd += (argument,)

        if cwd not in fs:
            fs[cwd] = 0

    elif re.match(file_pattern, line):
        size = re.findall(file_pattern, line)[0][0]

        for dir in fs.keys():
            if "/".join(cwd).startswith("/".join(dir)):
                fs[dir] += int(size)

used_space = fs[root]
needed_space = - (70_000_000 - 30_000_000 - used_space)

tmp_dir = root

for dir in fs.keys():
    if fs[dir] > needed_space and fs[dir] < fs[tmp_dir]:
        tmp_dir = dir

size_to_free = fs[tmp_dir]

print("Day 7 - size to free: ", size_to_free)
