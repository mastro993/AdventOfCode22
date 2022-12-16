# https://adventofcode.com/2022/day/1


def main():
    f = open("input01.txt", "r")
    lines = [l.rstrip() for l in f.readlines()]

    maxCalories = 0
    tmpCalories = 0

    for calories in lines:
        if calories == '':
            maxCalories = tmpCalories if tmpCalories > maxCalories else maxCalories
            tmpCalories = 0
        else:
            tmpCalories += int(calories)

    print("Day 1 - max calories: ", maxCalories)


if __name__ == "__main__":
    main()
