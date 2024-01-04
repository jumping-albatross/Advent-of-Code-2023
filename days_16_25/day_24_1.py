# day 24 (2023)
# https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html
import math

import numpy as np

print("Day 24 (2023). Hailstones.")

testing = False

if testing:
    raw = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
""".strip().splitlines()
else:
    with open('day_24.txt') as r:
        raw = r.read().strip().splitlines()


def process_raw_data():
    for hailstone in raw:
        position, velocity = hailstone.split("@")
        p = [int(p_raw) for p_raw in position.split(",")]
        v = [int(v_raw) for v_raw in velocity.split(",")]
        eq.append([p, v])


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

        try:
            ix = iy = math.inf
            vy, vx = vel_1[1], vel_1[0]

            ix, iy = np.linalg.solve(a, b)
            # print(f"    {(coeff_1, coeff_2)}{ix:.4f}, {iy:.4f}, {7 <= ix <= 27 and 7 <= iy <= 27}")

            vy, vx = vel_1[1], vel_1[0]
            dy, dx = iy - coord_1[1], ix - coord_1[0]

            if dx / abs(dx) != vx / abs(vx) and dy / abs(dy) != vy / abs(vy):
                intersect += m_min <= ix <= m_max and m_min <= iy <= m_max
            else:
                pass
                # print("same", f"{dx = }, {vx = }, {dy = }, {vy = }")

        except:
            print()
            vy, vx = vel_1[1], vel_1[0]
            dy, dx = coord_1[1] - iy, coord_1[0] - ix
            print(f"{dx = }, {vx = }, {dy = }, {vy = }")
            print(f"{dx / abs(dx) != vx / abs(vx) or dy / abs(dy) != vy / abs(vy) = }")
            print(f"{dy / dx = }, {vy / vx = }")
            print(f"    {(vel_1, vel_2)}{ix:.4f}, {iy:.4f}, {7 <= ix <= 27 and 7 <= iy <= 27}")
            print("Parallel line?")

print(f"Intersections: {intersect} (expected 2)")
print(f"{count = }, {len(eq) = }")
# 3857 too low
# 3861 too low
# 19690 too high
# 15833,15836 not right
