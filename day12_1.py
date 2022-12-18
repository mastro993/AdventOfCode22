# https://adventofcode.com/2022/day/12

from collections import deque

f = open("input12.txt", "r")
map = [list(l.rstrip()) for l in f.readlines()]

start = (0, 0)
end = (0, 0)

for y, row in enumerate(map):
    for x, char in enumerate(row):
        if char == "S":
            start = (y, x)
            map[y][x] = 'a'
        elif char == "E":
            end = (y, x)
            map[y][x] = 'z'

graph = {}

for y, row in enumerate(map):
    for x, char in enumerate(row):
        nodes = []
        for ny, nx in [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]:
            if ny < 0 or nx < 0 or ny >= len(map) or nx >= len(map[y]):
                continue
            if ord(map[ny][nx]) - ord(map[y][x]) <= 1:
                nodes.append((ny, nx))
        graph[(y, x)] = nodes


queue = deque()
queue.append((start, 0))
visited = set()

while queue:
    node, dist = queue.popleft()
    if node == end:
        print("Day 12 - Shortest path length:", dist)
        break
    if node in visited:
        continue
    visited.add(node)
    for n in graph[node]:
        queue.append((n, dist + 1))
