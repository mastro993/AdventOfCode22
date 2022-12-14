# https://adventofcode.com/2022/day/1


trees = []
trees_score = []


def scenic_score_from(tx, ty, dx, dy):
    height = trees[tx][ty]
    score = 0

    while True:
        tx += dx
        ty += dy

        if tx < 0 or tx >= len(trees):
            break

        if ty < 0 or ty >= len(trees[tx]):
            break

        if trees[tx][ty] >= height:
            score += 1
            break

        score += 1

    return score


def scenic_score_at(tx, ty):
    score = 1
    score *= scenic_score_from(tx, ty, 0, -1)
    score *= scenic_score_from(tx, ty, 0, 1)
    score *= scenic_score_from(tx, ty, -1, 0)
    score *= scenic_score_from(tx, ty, 1, 0)
    return score


def main():
    f = open("input8.txt", "r")
    rows = [l.rstrip() for l in f.readlines()]

    # Building trees
    for row in rows:
        trees.append([int(tree) for tree in list(row)])
        trees_score.append([0 for _ in list(row)])

    for x in range(0, len(trees)):
        for y in range(0, len(trees[x])):
            trees_score[x][y] = scenic_score_at(x, y)

    max_score = max(map(max, trees_score))

    print("Day 8 - max scenic score: ", max_score)


if __name__ == "__main__":
    main()
