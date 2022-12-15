# https://adventofcode.com/2022/day/9

import math
import copy


def move_from_direction(direction):
    if direction == "R":
        return (1, 0)
    elif direction == "L":
        return (-1, 0)
    elif direction == "U":
        return (0, 1)
    elif direction == "D":
        return (0, -1)


def main():
    f = open("input9t.txt", "r")
    lines = [l.rstrip() for l in f.readlines()]

    rope = [(0, 0)] * 10
    previous = [None] * 10
    visited = set()

    for line in lines:
        direction, steps = line.split(" ")
        move = move_from_direction(direction)

        for _ in range(int(steps)):
            previous[0] = copy.deepcopy(rope[0])
            rope[0] = (rope[0][0] + move[0], rope[0][1] + move[1])
            for i in range(1, len(rope)):
                distance = math.dist(rope[i - 1], rope[i])
                if distance >= 2:
                    previous[i] = copy.deepcopy(rope[i])
                    rope[i] = copy.deepcopy(previous[i - 1])
            visited.add(rope[len(rope) - 1])

    print("Day 9 - Tail visited ", len(visited), " block")


if __name__ == "__main__":
    main()
