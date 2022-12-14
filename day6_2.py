# https://adventofcode.com/2022/day/6


def main():
    f = open("input6.txt", "r")
    lines = [l.rstrip() for l in f.readlines()]

    data = ''

    for char in lines[0]:
        data += char
        buffer = data[len(data) - 14:len(data)]

        if len(buffer) < 14:
            continue

        if len(set(buffer)) == len(buffer):
            print("Day 6 - first repeated sequence after",
                  len(data), "characters")
            break


if __name__ == "__main__":
    main()
