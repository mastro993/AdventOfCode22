# https://adventofcode.com/2022/day/1

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
    f = open("input9.txt", "r")
    lines = [l.rstrip() for l in f.readlines()]

    head = (0, 0)
    tail = (0, 0)

    previous = None
    visited = set()

    for line in lines:
        direction, steps = line.split(" ")
        move = move_from_direction(direction)

        for _ in range(int(steps)):
            previous = copy.deepcopy(head)
            head = (head[0] + move[0], head[1] + move[1])
            distance = math.dist(head, tail)
            if distance >= 2:
                tail = copy.deepcopy(previous)
            visited.add(tail)

    print("Day 9 - Tail visited ", len(visited), " block")


if __name__ == "__main__":
    main()
