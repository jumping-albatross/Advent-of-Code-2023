# https://github.com/oloturia/AoC2023/blob/main/day21/part1.py
# https://www.reddit.com/r/adventofcode/comments/18o7014/comment/keylpbi/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
#
testing = False

if testing:
    grid = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
""".strip().split('\n')
else:
    with open('day_22.dat') as f:
        grid = f.read().strip().split('\n')

raw_coordinates = [x.split('~') for x in grid]
raw_coordinates = [[list(map(int, x[0].split(','))), list(map(int, x[1].split(',')))] for x in raw_coordinates]

# c = 557, rng = 4, lo = 0, hi = 9, idx = 0
# c = 554, rng = 4, lo = 0, hi = 9, idx = 1
# c = 134, rng = 4, lo = 1, hi = 308, idx = 2

heights = [[0] * 10 for _ in range(10)]
bricks = []

X, Y, Z = 0, 1, 2

# moral of the story: accept input data as is with only a minor sort
for u, v in raw_coordinates:
    lo = u[Z]
    uu = u
    vv = v
    bricks.append([lo, uu, vv])

bricks.sort()

for c in bricks[-1:-8:-1]:
    print(c)

# fall, round 1
for idx, (base, u, v) in enumerate(bricks):
    highest = 0
    for x in range(min(u[X], v[X]), max(u[X], v[X]) + 1):
        for y in range(min(u[Y], v[Y]), max(u[Y], v[Y]) + 1):
            highest = max(highest, heights[x][y] + 1)

    drop = min(u[Z], v[Z]) - highest

    for x in range(min(u[X], v[X]), max(u[X], v[X]) + 1):
        for y in range(min(u[Y], v[Y]), max(u[Y], v[Y]) + 1):
            heights[x][y] = highest + abs(u[Z] - v[Z])

    bricks[idx][0] = highest
    bricks[idx][1][Z] -= drop
    bricks[idx][2][Z] -= drop

print()

for c in bricks[-1:-8:-1]:
    print(c)

print()

for h in heights:
    print(h)

# disintegrate
dis_counter = 0
for dis_idx in range(len(bricks)):
    heights = [[0] * 10 for _ in range(10)]
    for idx, (base, u, v) in enumerate(bricks):
        if idx == dis_idx:
            continue
        highest = 0
        for x in range(min(u[X], v[X]), max(u[X], v[X]) + 1):
            for y in range(min(u[Y], v[Y]), max(u[Y], v[Y]) + 1):
                highest = max(highest, heights[x][y] + 1)

        drop = min(u[Z], v[Z]) - highest

        for x in range(min(u[X], v[X]), max(u[X], v[X]) + 1):
            for y in range(min(u[Y], v[Y]), max(u[Y], v[Y]) + 1):
                heights[x][y] = highest + abs(u[Z] - v[Z])
        if drop > 0:
            # print(f"Discarded: drop = {drop:>3}:base = {base:>3}, {u = }, {v =}, {dis_idx = }, {bricks[dis_idx] = }")
            break
    else:
        dis_counter += 1

print(f"{dis_counter = } (expected 441)")

# 441 correct
