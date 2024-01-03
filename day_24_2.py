# day 24 (2023)
# https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html
# https://stackoverflow.com/questions/31547657/how-can-i-solve-system-of-linear-equations-in-sympy
# https://github.com/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb
# https://docs.sympy.org/latest/tutorials/index.html

import numpy as np
import sympy

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


def signs_equal(g, h):
    """Return a boolean comparison of the signs of two numbers"""
    return np.sign(g) == np.sign(h)


# process paths
eq = []

process_raw_data()


def part_1_intersect_paths():
    m_min, m_max = (7, 27) if testing else (200000000000000, 400000000000000)
    _intersections = 0
    count = 0
    for i in range(len(eq)):
        for j in range(i + 1, len(eq)):
            count += 1

            (x1, y1, _), (vx1, vy1, _) = eq[i]
            (x2, y2, _), (vx2, vy2, _) = eq[j]

            m1 = vy1 / vx1
            m2 = vy2 / vx2

            b1 = -m1 * x1 + y1
            b2 = -m2 * x2 + y2

            a = np.array([[-m1, 1], [-m2, 1]])
            b = np.array([b1, b2])

            if vy1 / vx1 != vy2 / vx2:  # not parallel
                xi, yi = np.linalg.solve(a, b)

                dy1, dx1 = yi - y1, xi - x1
                dy2, dx2 = yi - y2, xi - x2

                if all((signs_equal(dx1, vx1), signs_equal(dy1, vy1),
                        signs_equal(dx2, vx2), signs_equal(dy2, vy2))):
                    _intersections += m_min <= xi <= m_max and m_min <= yi <= m_max
    print(f"{count = }, {len(eq) = }")
    return _intersections


print("Part 1 Solution")

intersections = part_1_intersect_paths()

ic = 2 if testing else 12938

print(f"Intersections: {intersections} (expected {ic})")

assert intersections == ic

# Part 2

"""
Unknown rock starting position and velocity: xr, yr, zr, vxr, vyr, vzr

Hailstone current position and velocity: xh, yh, zh, vxh, vyh, vzh

Note: hailstone's values are known so are substituted in

Time ties all the equations together since rock and hailstone collide...

1) xr + t * vxr = xh + t * vxh (they end up in the same place)
2) t * vxr - t * vxh = xh - xr
3) t * (vxr - vxh) = (xh - xr)
4) t = (xh - xr) / (vxr - vxh)

Repeat 1-4 for y and z

Ultimately:

(xh - xr) / (vxr - vxh) = (yh - yr) / (vyr - vyh) = (zh - zr) / (vzr - vzh)

Rearrange to eliminate potential for div 0 error.

(xh - xr) * (vyr - vyh) = (yh - yr) * (vxr - vxh)
(xh - xr) * (vzr - vzh) = (zh - zr) * (vxr - vxh)
(yh - yr) * (vzr - vzh) = (zh - zr) * (vyr - vyh)

Note: only need two of the three equations
"""

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr yr zr vxr vyr vzr")

stones = []
for hailstone in eq[:4]:  # minimum required is 4
    (xh, yh, zh), (vxh, vyh, vzh) = hailstone

    stones.append(sympy.Eq((xh - xr) * (vyr - vyh), (yh - yr) * (vxr - vxh)))  # equality
    stones.append(sympy.Eq((xh - xr) * (vzr - vzh), (zh - zr) * (vxr - vxh)))

s = sympy.solve(stones)[0]  # why a list?
x, y, z = s[xr], s[yr], s[zr]
cp = 47 if testing else 976976197397181

print()
print("Part 2 Solution")
print(f"{x = }, {y = }, {z = }")
print(f"{x + y + z} (expected {cp})")

assert x + y + z == cp
