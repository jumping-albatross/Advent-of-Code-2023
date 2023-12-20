# Day 18 Part 1
import math
import typing_extensions
from flood_fill import flood_fill

# flood_fill.flood_fill
dig_plan = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
""".strip().split("\n")

with open('data18.txt') as f:
    dig_plan = f.read().strip().split('\n')

directions = [x.split(' ')[:2] for x in dig_plan]

digger : list[int] = [0,0]
trench = [tuple(digger)]

DIR = {'D' : (1, 0), 'U' : (-1, 0), 'L' : (0, -1), 'R' : (0, 1)}

r_min, r_max = math.inf, -math.inf
c_min, c_max = math.inf, -math.inf

for (dir, dist) in directions:
    cr, cc = trench[-1]
    dr, dc = DIR[dir]
    for i in range(1, int(dist) + 1):
        trench.append((cr + dr * i, cc + dc * i))
        r_min = min(r_min, trench[-1][0])
        c_min = min(c_min, trench[-1][1])
        r_max = max(r_max, trench[-1][0])
        c_max = max(c_max, trench[-1][1])

print(f"{(r_min, c_min) = },   {(r_max, c_max) = }")

grid = [[0 for _ in range(c_max - c_min + 1)] for _ in range(r_max - r_min + 1)]

for (r, c) in trench:
    grid[r-r_min][c-c_min] = 1 #'■'

t = 0
for g in grid:
    t += sum(g)
#     print(g)
print(f"Part 1: {t}")
print()

flood_fill(grid, 150,150,0,1)#'.','■')

t = 0
for g in grid:
    # print(g)
    t += sum(g)
print()
print(f"Part 1: {t}")

for r in range(120, 150):
  for c in range(100, 150):
    print(grid[r][c], end='')
  print()