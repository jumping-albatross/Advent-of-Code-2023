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
#....#..#""".split(
    "\n\n"
)

# . == ash # == rock
with open("data13.txt") as r:
    raw = r.read().split("\n\n")


def rotate_90(pattern):
    t = []
    for line in pattern:
        t.append(list(line))
    _v = list(zip(*t))
    return ["".join(x) for x in _v]


patterns = []

for pattern in raw:
    pattern = pattern.split("\n")
    h = []

    for line in pattern:
        line = line.replace('.', '0')
        line = line.replace('#', '1')
        h.append(line)
    patterns.append(h)

def find_mirror(p):
    # 1 initial pass to find matching sequential rows
    matches = []
    for i in range(len(p) - 1):
        if p[i] == p[i + 1]:
            matches.append(i)
    print(matches)
    # 2 for each matching sequential row loop up/down
    # to the shortest distance

    for m in matches:
        for i in range(min(m + 1, len(p) - m - 1)):
            if p[m-i] != p[m + 1 + i]:
                break
        else:
            return (m + 1)
    return 0

columns_sum = []
rows_sum = []
for p in patterns:
    rows_sum.append(find_mirror(p))
    columns_sum.append(find_mirror(rotate_90(p)))
print('c', columns_sum)
print('r', rows_sum)

print(sum(columns_sum) + sum(rows_sum) * 100)

# print(f"Part 1:\nObserved = {}")
# print("Expected = {}")
# print("{}")
