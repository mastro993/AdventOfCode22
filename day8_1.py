# https://adventofcode.com/2022/day/1

map = []


def is_visible_from_top(tx, ty):
    height = map[tx][ty]

    for x in range(0, tx):
        if map[x][ty] >= height:
            return False

    return True


def is_visible_from_bottom(tx, ty):
    height = map[tx][ty]

    for x in range(tx + 1, len(map)):
        if map[x][ty] >= height:
            return False

    return True


def is_visible_from_left(tx, ty):
    height = map[tx][ty]

    for y in range(0, ty):
        if map[tx][y] >= height:
            return False

    return True


def is_visible_from_right(tx, ty):
    height = map[tx][ty]

    for y in range(ty + 1, len(map[tx])):
        if map[tx][y] >= height:
            return False

    return True


def is_visible_at(tx, ty):
    is_visible = is_visible_from_left(tx, ty) or is_visible_from_right(
        tx, ty) or is_visible_from_top(tx, ty) or is_visible_from_bottom(tx, ty)
    return is_visible


def main():
    f = open("input8.txt", "r")
    rows = [l.rstrip() for l in f.readlines()]

    # Building trees map
    for row in rows:
        trees = []
        for tree in row:
            trees.append(int(tree))
        map.append(trees)

    map_perimeter_size = (len(map) - 1) * 2 + (len(map[0]) - 1) * 2
    visible_trees = map_perimeter_size

    for x in range(1, len(map) - 1):
        for y in range(1, len(map[x]) - 1):
            visible_trees += 1 if is_visible_at(x, y) else 0

    # 1805

    print("Day 8 - visible trees: ", visible_trees)


if __name__ == "__main__":
    main()
