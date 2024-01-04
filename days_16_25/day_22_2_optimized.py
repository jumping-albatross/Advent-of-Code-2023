# https://github.com/oloturia/AoC2023/blob/main/day21/part1.py
# https://www.reddit.com/r/adventofcode/comments/18o7014/comment/keylpbi/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# https://github.com/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb

import copy
import time

print("Day 22 (2023): Jenga", "\n")

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
    with open('day_22.txt') as f:
        grid = f.read().strip().split('\n')

raw_coordinates = [x.split('~') for x in grid]
raw_coordinates = [[list(map(int, x[0].split(','))), list(map(int, x[1].split(',')))] for x in raw_coordinates]

# moral of the story: accept input data as is with only a minor sort
X, Y, Z = 0, 1, 2

bricks = [[u[Z], u, v] for u, v in raw_coordinates]
bricks.sort()


# X c = 557, rng = 4, lo = 0, hi = 9,   idx = 0
# Y c = 554, rng = 4, lo = 0, hi = 9,   idx = 1
# Z c = 134, rng = 4, lo = 1, hi = 308, idx = 2

def drop_all_bricks(_bricks, _topo_map=None):
    """Drops all bricks to their lowest height in the given Jenga stack"""
    if _topo_map is None:
        _topo_map = [[0] * 10 for _ in range(10)]

    falls = 0

    for idx, (brick_base, u, v) in enumerate(_bricks):
        fall_distance, highest_elev = drop_one_brick(_topo_map, u, v)

        _bricks[idx][0] = highest_elev
        _bricks[idx][1][Z] -= fall_distance
        _bricks[idx][2][Z] -= fall_distance

        falls += fall_distance > 0

    return falls


def drop_one_brick(_topo_map, u, v):
    highest_elev = 0

    for x in range(min(u[X], v[X]), max(u[X], v[X]) + 1):
        for y in range(min(u[Y], v[Y]), max(u[Y], v[Y]) + 1):
            highest_elev = max(highest_elev, _topo_map[x][y] + 1)

    fall_distance = min(u[Z], v[Z]) - highest_elev

    for x in range(min(u[X], v[X]), max(u[X], v[X]) + 1):
        for y in range(min(u[Y], v[Y]), max(u[Y], v[Y]) + 1):
            _topo_map[x][y] = highest_elev + abs(u[Z] - v[Z])

    return fall_distance, highest_elev


print("Top 2 bricks, before fall")
for c in bricks[-1:-3:-1]:
    print(c)

t1 = time.time_ns()
drop_all_bricks(bricks)
t2 = time.time_ns()

print("\nTop 2 bricks, after fall")
for c in bricks[-1:-3:-1]:
    print(c)

print()

disintegrate_ok_sum = 0
bricks_fall_sum = 0

# TO DO optimize this nested for loop to avoid re-building heights each time

t3 = time.time_ns()
topo_map_original = [[0] * 10 for _ in range(10)]

for dis_idx in range(len(bricks)):
    topo_map = copy.deepcopy(topo_map_original)

    for idx, (base, u, v) in enumerate(bricks[dis_idx + 1:]):
        highest = 0

        for x in range(min(u[X], v[X]), max(u[X], v[X]) + 1):
            for y in range(min(u[Y], v[Y]), max(u[Y], v[Y]) + 1):
                highest = max(highest, topo_map[x][y] + 1)

        drop = min(u[Z], v[Z]) - highest

        if drop > 0:
            # part 2: see how many other bricks fall when this one is disintegrated
            bricks_fall_sum += drop_all_bricks(copy.deepcopy(bricks[dis_idx + 1 + idx:]),
                                               _topo_map=copy.deepcopy(topo_map))

        for x in range(min(u[X], v[X]), max(u[X], v[X]) + 1):
            for y in range(min(u[Y], v[Y]), max(u[Y], v[Y]) + 1):
                topo_map[x][y] = highest + abs(u[Z] - v[Z])

        if drop > 0:
            # part 1: bricks fall after disintegration, not safe to disintegrate
            break
    else:
        disintegrate_ok_sum += 1

    drop_one_brick(topo_map_original, bricks[dis_idx][1], bricks[dis_idx][2])

t4 = time.time_ns()

print()
print(f"Drop all tiles: {(t2 - t1) / 1e9:.4f} s and disintegrate all tiles {(t4 - t3) / 1e9:.4f} s")
# Unoptimized: Drop all tiles: 0.0170 s and disintegrate all tiles 15.8034 s
# Optimized:   Drop all tiles: 0.0157 s and disintegrate all tiles 9.3558 s
print()
print(f"Part 1: {disintegrate_ok_sum = } (expected 5 for test; 441 for full data set)")
print(f"Part 2: {bricks_fall_sum = } (expected 7 for test; 80778 for full data set)")
