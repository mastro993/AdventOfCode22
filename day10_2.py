# https://adventofcode.com/2022/day/10

crt_width = 40
crt_height = 6


def main():
    f = open("input10.txt", "r")
    lines = [l.rstrip() for l in f.readlines()]

    crt = [["." for _ in range(crt_width)] for _ in range(crt_height)]
    stack = []
    x = 1

    for cycle_n in range(240):

        line = lines[cycle_n % len(lines)]

        if line.startswith("noop"):
            stack.append(0)
        if line.startswith("addx"):
            _, value = line.split(" ")
            stack.extend([0, int(value)])

        if x - 1 <= (cycle_n % crt_width) <= x + 1:
            crt[cycle_n // crt_width][cycle_n % crt_width] = "#"

        cycle_n += 1

        if len(stack) > 0:
            x += stack.pop(0)

    for row in crt:
        print("".join(row))


if __name__ == "__main__":
    main()
