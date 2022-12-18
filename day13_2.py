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


def quicksort(packets):
    if len(packets) <= 1:
        return packets

    pivot = packets[0]
    left = []
    right = []

    for packet in packets[1:]:
        if is_right_order(eval(packet), eval(pivot)) < 0:
            left.append(packet)
        else:
            right.append(packet)

    return quicksort(left) + [pivot] + quicksort(right)


f = open("input13.txt", "r")
packets = [stripped for line in f if (stripped := line.strip())]
packets.extend(["[[2]]", "[[6]]"])

packets = quicksort(packets)

i1 = packets.index("[[2]]") + 1
i2 = packets.index("[[6]]") + 1

result = i1 * i2

print("Day 13 - Result:", result)
