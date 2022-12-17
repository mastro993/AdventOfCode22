# https://adventofcode.com/2022/day/3


def priority(char): return ord(char) - \
    96 if ord(char) - 96 > 0 else ord(char) - 38


f = open("input03.txt", "r")
lines = [l.rstrip() for l in f.readlines()]

priority_sum = 0

for line in lines:
    first, second = line[:len(line)//2], line[len(line)//2:]
    type = list(set(first) & set(second))
    priority_sum += priority(type[0])

print("Day 3 - priority sum: ", priority_sum)
