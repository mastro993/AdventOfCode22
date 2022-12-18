# https://adventofcode.com/2022/day/13

def as_list(x): return x if type(x) == list else [x]


def is_right_order(left, right):

    if type(left) == int and type(right) == int:
        return left - right

    left = as_list(left)
    right = as_list(right)

    for l, r in zip(left, right):
        result = is_right_order(l, r)
        if result != 0:
            return result

    return len(left) - len(right)


f = open("input13.txt", "r")
data = f.read().split("\n\n")

sum = 0

for index, pair in enumerate(data):
    left, right = pair.split("\n")
    sum += index + 1 if is_right_order(eval(left), eval(right)) < 0 else 0

print("Day 13 - Sum of right orders:", sum)
