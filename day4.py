# https://adventofcode.com/2022/day/4


def main():
    f = open("input4.txt", "r")
    lines = [l.rstrip() for l in f.readlines()]

    count = 0

    for line in lines:
        s = []
        e = []
        for range in line.split(","):
            start, end = range.split("-")
            s.append(int(start))
            e.append(int(end))

        if s[0] <= s[1] <= e[1] <= e[0]:
            count += 1
        elif s[1] <= s[0] <= e[0] <= e[1]:
            count += 1
        elif s[1] <= s[0] <= e[1] <= e[0]:
            count += 1
        elif s[0] <= s[1] <= e[0] <= e[1]:
            count += 1
        
    print("Day 4 - overlapping ranges: ", count)


if __name__ == "__main__":
    main()