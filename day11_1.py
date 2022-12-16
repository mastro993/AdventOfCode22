# https://adventofcode.com/2022/day/11

import re

monkey_pattern = r"Monkey [0-9]*:\n.*items: ([0-9,\s]*)\n.*new = (.*)\n.*divisible by ([0-9]*)\n.*monkey ([0-9]*)\n.*monkey ([0-9]*)"


def get_operation(text):
    _, op, value = text.split(" ")
    match op:
        case "+": return lambda x: int(value) + x
        case "-": return lambda x: int(value) - x
        case "*": return lambda x: x * x if value == "old" else x * int(value)


def test_level(
    monkey, level): return monkey[3] if level % monkey[2] == 0 else monkey[4]


def main():
    f = open("input11.txt", "r")
    data = f.read()

    monkeys = []

    for items, operation, test, if_true, if_false in re.findall(monkey_pattern, data):
        monkeys.append([
            [int(x) for x in items.split(", ")],
            get_operation(operation),
            int(test),
            int(if_true),
            int(if_false),
            0
        ])

    for _ in range(20):
        for monkey in monkeys:
            while monkey[0]:
                item = monkey[0].pop(0)
                lvl = monkey[1](item) // 3
                dest = test_level(monkey, lvl)
                monkeys[dest][0].append(lvl)
                monkey[5] += 1

    monkeys = sorted(monkeys, key=lambda x: x[5], reverse=True)

    print("Day 11 - Total level: ", monkeys[0][5] * monkeys[1][5])


if __name__ == "__main__":
    main()
