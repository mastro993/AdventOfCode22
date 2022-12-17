# https://adventofcode.com/2022/day/3


def priority(char): return ord(char) - \
    96 if ord(char) - 96 > 0 else ord(char) - 38


f = open("input03.txt", "r")
lines = [l.rstrip() for l in f.readlines()]

priority_sum = 0

it = iter(lines)
for line in it:
    type = list(set(line) & set(next(it)) & set(next(it)))
    priority_sum += priority(type[0])

print("Day 3 - priority sum: ", priority_sum)
