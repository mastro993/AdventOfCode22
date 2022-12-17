# https://adventofcode.com/2022/day/6


f = open("input06.txt", "r")
data = f.read()

for i in range(4, len(data)):
    buffer = data[i-4:i]

    if len(set(buffer)) == len(buffer):
        print("Day 6 - first repeated sequence after", i, "characters")
        break
