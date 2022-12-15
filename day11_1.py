# https://adventofcode.com/2022/day/11

import re

monkey_pattern = r"Monkey [0-9]*:\n.*items: ([0-9,\s]*)\n.*new = (.*)\n.*divisible by ([0-9]*)\n.*monkey ([0-9]*)\n.*monkey ([0-9]*)"


def get_operation(text):
    _, op, value = text.split(" ")
    match op:
        case "+": return lambda x: int(value) + x
        case "-": return lambda x: int(value) - x
        case "*": return lambda x: x * x if value == "old" else x * int(value)


def main():
    f = open("input11.txt", "r")

    matches = re.findall(monkey_pattern, f.read())
    monkeys = []

    for match in matches:
        items = [int(x) for x in match[0].split(", ")]
        operation = get_operation(match[1])
        test = int(match[2])
        iftrue = int(match[3])
        iffalse = int(match[4])

        monkeys.append([items, operation, test, iftrue, iffalse, 0])

    for _ in range(20):
        for monkey in monkeys:
            for _ in range(len(monkey[0])):
                item = monkey[0].pop(0)
                worry_level = monkey[1](item) // 3
                if worry_level % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(worry_level)
                else:
                    monkeys[monkey[4]][0].append(worry_level)
                monkey[5] += 1

    monkeys = sorted(monkeys, key=lambda x: x[5], reverse=True)

    print("Day 11 - Total level: ", monkeys[0][5] * monkeys[1][5])


if __name__ == "__main__":
    main()
