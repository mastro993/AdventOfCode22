# https://adventofcode.com/2022/day/9

import math
import copy

moves = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


f = open("input09.txt", "r")
lines = [l.rstrip() for l in f.readlines()]

head = (0, 0)
tail = (0, 0)

previous = None
visited = set()

for line in lines:
    direction, steps = line.split(" ")
    move = moves[direction]

    for _ in range(int(steps)):
        previous = copy.deepcopy(head)
        head = (head[0] + move[0], head[1] + move[1])
        distance = math.dist(head, tail)
        if distance >= 2:
            tail = copy.deepcopy(previous)
        visited.add(tail)

print("Day 9 - Tail visited ", len(visited), " block")
