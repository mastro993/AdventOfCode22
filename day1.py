# https://adventofcode.com/2022/day/1


def main():
    f = open("input1.txt", "r")
    lines = [l.rstrip() for l in f.readlines()]

    topCalories = [0,0,0]
    tmpCalories = 0

    for calories in lines:
        if calories == '':
            topCalories.append(tmpCalories)
            topCalories.sort()
            topCalories.pop(0)
            tmpCalories = 0
        else:
            tmpCalories += int(calories)

    print("Day 1 - top calories: ", topCalories, ", sum calories: ", sum(topCalories))


if __name__ == "__main__":
    main()