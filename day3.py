# https://adventofcode.com/2022/day/3

lines_count = 3


def priority(char): return ord(char) - \
    96 if ord(char) - 96 > 0 else ord(char) - 38


def main():
    f = open("input3.txt", "r")
    lines = [l.rstrip() for l in f.readlines()]

    priority_sum = 0
    tmp_lines = []

    for line in lines:
        tmp_lines.append(line)

        if (len(tmp_lines) == lines_count):
            type = list(set(tmp_lines[0]) & set(
                tmp_lines[1]) & set(tmp_lines[2]))
            priority_sum += priority(type[0])
            tmp_lines = []

    print("Day 3 - priority sum: ", priority_sum)


if __name__ == "__main__":
    main()
