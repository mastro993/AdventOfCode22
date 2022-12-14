# https://adventofcode.com/2022/day/3

lines_count = 3


def priority(char): return ord(char) - \
    96 if ord(char) - 96 > 0 else ord(char) - 38


def main():
    f = open("input3.txt", "r")
    lines = [l.rstrip() for l in f.readlines()]

    priority_sum = 0

    for line in lines:
        # split line in two string
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        type = list(set(firstpart) & set(secondpart))
        priority_sum += priority(type[0])

    print("Day 3 - priority sum: ", priority_sum)


if __name__ == "__main__":
    main()
