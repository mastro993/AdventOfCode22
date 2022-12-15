# https://adventofcode.com/2022/day/10


def main():
    f = open("input10.txt", "r")
    lines = [l.rstrip() for l in f.readlines()]

    stack = []
    x = 1
    cycle_n = 0

    signal_strength_sum = 0
    checkpoints = [20, 60, 100, 140, 180, 220]

    while True:

        line = lines[cycle_n % len(lines)]

        if line.startswith("noop"):
            stack.append(0)
        if line.startswith("addx"):
            _, value = line.split(" ")
            stack.extend([0, int(value)])

        cycle_n += 1

        if ((cycle_n) in checkpoints):
            signal_strength_sum += x * (cycle_n)
            checkpoints.remove(cycle_n)

        if len(checkpoints) == 0:
            break

        if len(stack) > 0:
            x += stack.pop(0)

    print(signal_strength_sum)


if __name__ == "__main__":
    main()
