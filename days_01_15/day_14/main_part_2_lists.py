raw = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".split("\n")

# with open("data14.txt") as r:
#     raw = r.read().split("\n")

rocks = []
for r in range(len(raw)):
    for c in range(len(raw[0])):
        if raw[r][c] != '.':
            rocks.append([r, c, raw[r][c]])

import operator


def tilt(v, h):
    '''v==-1 up, 0 nothing, 1 down
    h==-1 left, 0 nothin, 1 right'''

    R, C = 0, 1
    if v != 0 and h == 0:
        # sort for vertical tilt
        rocks.sort(key = operator.itemgetter(C, R))
    else:
        # sort for horizontal tilt
        rocks.sort(key = operator.itemgetter(R, C))

    rc, sub_idx = 0, 0
    for i in range(len(rocks)):
        sub_idx += 1
        if rc != rocks[i][2]:
            rc = rocks[i][2]
            sub_idx = 0
            
changes = -1
while changes != None:
    changes = tilt(-1, 0)
    print(changes)

print("Part 1:\n")

# for r in platform:
#     print(''.join(r))

load = 0
pl = len(platform)
for i, line in enumerate(platform):
    load += (pl - i) * ''.join(line).count('O')

print()
print("Part 1 load", load)
