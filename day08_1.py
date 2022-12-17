# https://adventofcode.com/2022/day/8


edges = [(0, -1), (0, 1), (-1, 0), (1, 0)]
trees = []


def is_visible_from(tx, ty, edge):
    height = trees[tx][ty]

    while True:
        tx += edge[0]
        ty += edge[1]

        if tx < 0 or tx >= len(trees):
            return True

        if ty < 0 or ty >= len(trees[tx]):
            return True

        if trees[tx][ty] >= height:
            return False


def is_visible_at(tx, ty):

    for edge in edges:
        if is_visible_from(tx, ty, edge):
            return True

    return False


f = open("input08.txt", "r")
trees = [list(l.rstrip()) for l in f.readlines()]

visible_trees = 0

for x in range(0, len(trees)):
    for y in range(0, len(trees[x])):
        if is_visible_at(x, y):
            visible_trees += 1

print("Day 8 - visible trees: ", visible_trees)
