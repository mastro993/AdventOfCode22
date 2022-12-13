# https://adventofcode.com/2022/day/1

packet_size = 14


def main():
    f = open("input6.txt", "r")
    lines = [l.rstrip() for l in f.readlines()]

    data = ''

    for char in lines[0]:
        data += char
        buffer = data[len(data) - packet_size:len(data)]

        if len(buffer) < packet_size:
            continue

        if len(set(buffer)) == len(buffer):
            print("Day 6 - first repeated sequence after",
                  len(data), "characters: ")
            break


if __name__ == "__main__":
    main()
