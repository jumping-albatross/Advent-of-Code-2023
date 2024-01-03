# day 24 (2023)
# https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html
import math
from itertools import combinations

import numpy as np

print("Day 24 (2023). Hailstones.")

testing = False

if testing:
    r_raw = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
""".strip()
    raw = r_raw.splitlines()
else:
    with open('day_24.txt') as r:
        r_raw = r.read().strip()
        raw = r_raw.splitlines()


def process_raw_data():
    for hailstone in raw:
        position, velocity = hailstone.split("@")
        p = [int(p_raw) for p_raw in position.split(",")]
        v = [int(v_raw) for v_raw in velocity.split(",")]
        eq.append([p, v])


def part1(puzzle_input, test_input=False):
    hailstones = []
    for line in puzzle_input.split('\n'):
        nums = line.replace('@', ',').split(',')
        hailstones.append(tuple(map(int, nums)))

    if test_input:
        lo, hi = 7, 27
    else:
        lo, hi = 2e14, 4e14

    total = 0
    for h1, h2 in combinations(hailstones, 2):
        x1, y1, _, dx1, dy1, _ = h1
        x2, y2, _, dx2, dy2, _ = h2
        m1 = dy1 / dx1
        m2 = dy2 / dx2
        if m1 == m2:  # they move in parallel and never meet
            continue
        b1 = y1 - m1 * x1
        b2 = y2 - m2 * x2
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        if total == 0:
            print(x, y)

        if all((lo <= x <= hi,  # x and y need to be in range
                lo <= y <= hi,
                (x > x1 and dx1 > 0) or (x < x1 and dx1 < 0),  # intersection needs to happen in the future
                (x > x2 and dx2 > 0) or (x < x2 and dx2 < 0))):
            total += 1

    return total


print("Other solution", part1(r_raw, test_input=testing))

# process paths
eq = []
process_raw_data()

print("""Expected:
Hailstone A: 19, 13, 30 @ -2, 1, -2
Hailstone B: 18, 19, 22 @ -1, -1, -2
Hailstones' paths will cross inside the test area (at x=14.333, y=15.333).
""")

intersect = 0
m_min, m_max = (7, 27) if testing else (200000000000000, 400000000000000)

count = 0
for i in range(len(eq)):
    for j in range(i + 1, len(eq)):
        count += 1

        coord_1, vel_1 = eq[i]
        coord_2, vel_2 = eq[j]

        x1, y1 = vel_1[1] / vel_1[0], 1
        x2, y2 = vel_2[1] / vel_2[0], 1

        # y = mx + b
        # by = ax + c
        # b = y - mx

        b1 = -x1 * coord_1[0] + y1 * coord_1[1]
        b2 = -x2 * coord_2[0] + y2 * coord_2[1]

        # a1x + b1y = c1
        # a2x + b2y = c2

        a = np.array([[-x1, y1], [-x2, y2]])
        b = np.array([b1, b2])

        xi = yi = math.inf

        v1x, v1y, _ = vel_1
        v2x, v2y, _ = vel_2

        x1, y1, _ = coord_1
        x2, y2, _ = coord_2

        if v1y / v1x != v2y / v2x:
            xi, yi = np.linalg.solve(a, b)

            d1y, d1x = yi - y1, xi - x1
            d2y, d2x = yi - y2, xi - x2

            # print(f"    {(coord_1, coord_2)}")
            # print(f"{ix:.4f} {iy:.4f}, {7 <= ix <= 27 and 7 <= iy <= 27}")


            if round(d1x / abs(d1x), 0) == round(v1x / abs(v1x), 0) and round(d1y / abs(d1y), 0) == round(v1y / abs(v1y), 0) and \
                    round(d2x / abs(d2x), 0) == round(v2x / abs(v2x), 0) and round(d2y / abs(d2y), 0) == round(v2y / abs(v2y), 0):
                intersect += m_min <= xi <= m_max and m_min <= yi <= m_max

            d1y, d1x = coord_1[1] - yi, coord_1[0] - xi
            # print(f"{dx = }, {vx = }, {dy = }, {vy = }")
            # print(f"{dx / abs(dx) != vx / abs(vx) or dy / abs(dy) != vy / abs(vy) = }")
            # print(f"{dy / dx = }, {vy / vx = }")
            # print(f"    {(vel_1, vel_2)}{ix:.4f}, {iy:.4f}, {7 <= ix <= 27 and 7 <= iy <= 27}")
            # print("Parallel line?")
        else:
            print('parallel?')
print(f"Intersections: {intersect} (expected 2)")
print(f"{count = }, {len(eq) = }")
# 3857 too low
# 3861 too low
# 19690 too high
# 15833,15836 not right
