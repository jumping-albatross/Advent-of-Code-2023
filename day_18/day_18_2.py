# Day 18 Part 2
import math

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

directions = [(int('0x' + x.split('#')[1][:5], 16),
               'RDLU'[int(x.split('#')[1][5:6])])
              for x in dig_plan]

digger: list[int] = [0, 0]
trench = [tuple(digger)]

DIR = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}


for (dist, dir) in directions:
    cr, cc = trench[-1]
    dr, dc = DIR[dir]
    trench.append((cr + dr * dist, cc + dc * dist))

print('/' + '=' * 35 + '\\')
print(f"|{'Directions':>14}  {'Vertices'}          |")
print('|' + '=' * 35 + '|')
print(f"{'':>15}  {trench[0]}")

for i, (d, t) in enumerate(zip(directions, trench[1:])):
    if i < 10 or i > len(trench) - 10:
        print(f"{str(d):>15}  {t}")
    elif i < 11:
        print(' ' * 6 + '.' * 20)

print('=' * 35)

# 0.5 × |x1y2 - y1x2 + x2y3 - y2x3 + ... + xny1 - ynx1|
# https://www.omnicalculator.com/math/irregular-polygon-area
# Shoelace theorem or Gauss' formula

area = 0

for i in range(len(trench) - 1):
    y1, x1 = trench[i]
    y2, x2 = trench[i + 1]
    
    area += x1 * y2
    area -= y1 * x2

print('Sample data = 952408144115')

perimeter = sum([j for (j, _) in directions])

print(f"{'Part 2:':>14} {area // 2 + perimeter // 2 + 1 = }")


# Anton's code
places = trench[:]
total = 0
for i in range(len(places)):
    y1, x1 = places[i]
    y2, x2 = places[(i + 1) % len(places)]

    total -= (y1 * x2) - (x1 * y2) # area
    total += abs(x1 - x2) + abs(y1 - y2) # perimeter

print(f"{'Anton answer:':>14} {int(total/2) + 1 = }")