# https://adventofcode.com/2022/day/8


trees = []


def is_visible_from(tx, ty, dx, dy):
    height = trees[tx][ty]

    while True:
        tx += dx
        ty += dy

        if tx < 0 or tx >= len(trees):
            return True

        if ty < 0 or ty >= len(trees[tx]):
            return True

        if trees[tx][ty] >= height:
            return False


def is_visible_at(tx, ty):

    if is_visible_from(tx, ty, 0, -1):
        return True

    if is_visible_from(tx, ty, 0, 1):
        return True

    if is_visible_from(tx, ty, -1, 0):
        return True

    if is_visible_from(tx, ty, 1, 0):
        return True

    return False


def main():
    f = open("input8.txt", "r")
    rows = [l.rstrip() for l in f.readlines()]

    # Building trees
    for row in rows:
        trees.append([int(tree) for tree in list(row)])

    visible_trees = 0

    for x in range(0, len(trees)):
        for y in range(0, len(trees[x])):
            if is_visible_at(x, y):
                visible_trees += 1

    print("Day 8 - visible trees: ", visible_trees)


if __name__ == "__main__":
    main()
