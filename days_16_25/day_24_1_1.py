# day 24 (2023)
# https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html

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
    with open('day_24.dat') as r:
        r_raw = r.read().strip()
        raw = r_raw.splitlines()


def process_raw_data():
    for hailstone in raw:
        position, velocity = hailstone.split("@")
        p = [int(p_raw) for p_raw in position.split(",")]
        v = [int(v_raw) for v_raw in velocity.split(",")]
        eq.append([p, v])


def sign_compare(g, h):
    """Return a boolean comparison of the signs of two numbers"""
    return np.sign(g) == np.sign(h)


# process paths
eq = []

process_raw_data()

m_min, m_max = (7, 27) if testing else (200000000000000, 400000000000000)

intersect = 0
count = 0

for i in range(len(eq)):
    for j in range(i + 1, len(eq)):
        count += 1

        coord_1, vel_1 = eq[i]
        coord_2, vel_2 = eq[j]

        v1x, v1y, _ = vel_1
        v2x, v2y, _ = vel_2

        x1, y1, _ = coord_1
        x2, y2, _ = coord_2

        m1 = v1y / v1x
        m2 = v2y / v2x

        b1 = -m1 * x1 + y1
        b2 = -m2 * x2 + y2

        a = np.array([[-m1, 1], [-m2, 1]])
        b = np.array([b1, b2])

        if v1y / v1x != v2y / v2x:  # not parallel
            xi, yi = np.linalg.solve(a, b)

            d1y, d1x = yi - y1, xi - x1
            d2y, d2x = yi - y2, xi - x2

            if sign_compare(d1x, v1x) and sign_compare(d1y, v1y) and sign_compare(d2x, v2x) and sign_compare(d2y, v2y):
                intersect += m_min <= xi <= m_max and m_min <= yi <= m_max

tv = 2 if testing else 12938
assert intersect == tv

print(f"{count = }, {len(eq) = }")
print(f"Intersections: {intersect} (expected {tv})")
