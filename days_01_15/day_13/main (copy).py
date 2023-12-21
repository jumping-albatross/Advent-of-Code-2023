raw = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".split("\n\n")

# . == ash # == rock
with open("data13.txt") as r:
    raw = r.read().split("\n\n")

patterns = [pattern.split("\n") for pattern in raw]

def rotate_90(pattern):
    t = [list(line) for line in pattern]
    return ["".join(x) for x in list(zip(*t))]


def find_mirror(p):
    # 1 initial pass to find matching sequential rows
    matches = []
    for i in range(len(p) - 1):
        if p[i] == p[i + 1]:
            matches.append(i)

    # 2 for each matching sequential row loop up/down
    for m in matches[::-1]:
        for i in range(min(m + 1, len(p) - m - 1)):
            if p[m - i] != p[m + 1 + i]:
                matches.remove(m)
                break

    for i in range(len(matches)):
        matches[i] += 1
        
    return matches


def flatten(arr):
    _n = []
    for _1 in arr:
        for _2 in _1:
            _n.append(_2)
    return _n


def brute_force(p):
    """modifies every cell in the pattern
    and identifies all mirrors"""

    rm_1 = find_mirror(p)
    cm_1 = find_mirror(rotate_90(p))

    if len(rm_1) > 1:
        rm_1.remove([])
        rm_1 = rm_1[0]

    if len(cm_1) > 1:
        cm_1.remove([])
        cm_1 = cm_1[0]

    row_mirror = []
    col_mirror = []

    for r in range(len(p)):
        for c in range(len(p[0])):
            # Invert current r, c
            temp_1 = p[r]
            temp = list(temp_1)
            temp[c] = "#" if temp[c] == "." else "."
            p[r] = "".join(temp)

            row_mirror.append(find_mirror(p))
            col_mirror.append(find_mirror(rotate_90(p)))

            # Done. Revert to original
            p[r] = temp_1

    row_mirror = set(flatten(row_mirror))
    col_mirror = set(flatten(col_mirror))
    
    if len(row_mirror) + len(col_mirror) > 1:
        for v in rm_1:
            if v in row_mirror:
                row_mirror.remove(v)
        for v in cm_1:
            if v in col_mirror:
                col_mirror.remove(v)

    if len(row_mirror) > 0 or len(col_mirror) > 0:
        a = list(row_mirror)[0] if len(row_mirror) > 0 else 0
        b = list(col_mirror)[0] if len(col_mirror) > 0 else 0
        return a, b
    else:
        raise Exception(f"No mirror found, (r, c) = ({r}, {c})")


# Part 1

columns_sum_1 = []
rows_sum_1 = []

for p in patterns:
    rows_sum_1.append(find_mirror(p))
    columns_sum_1.append(find_mirror(rotate_90(p)))

print("Part 1:\n")

s1 = sum(flatten(rows_sum_1))
s2 = sum(flatten(columns_sum_1))

print(s1 + s2 * 100)
print()

# Part 2

columns_sum = []
rows_sum = []

for p in patterns:
    row_mirror, col_mirror = brute_force(p)
    rows_sum.append(row_mirror)
    columns_sum.append(col_mirror)

print("Part 2:\n")
print(sum(columns_sum) + sum(rows_sum) * 100)