raw = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split("\n")

with open("day_11.dat") as r:
    raw = r.read().split("\n")

matrix = [list(x) for x in raw]
matrix_transpose = list(zip(*raw))

rows = []
cols = []

for i, m in enumerate(matrix):
    if len(set(m)) == 1:
        rows.append(i)

for i, m in enumerate(matrix_transpose):
    if len(set(m)) == 1:
        cols.append(i)

stars = []
for r, line in enumerate(matrix):
    for c, v in enumerate(line):
        if v == "#":
            stars.append([r, c])

ROW = 0
COL = 1
# Apply translations to stars
for row in rows[::-1]:
    for i, star in enumerate(stars):
        if star[ROW] >= row:
            stars[i][ROW] += 1000000 - 1

for col in cols[::-1]:
    for i, star in enumerate(stars):
        if star[COL] >= col:
            stars[i][COL] += 1000000 - 1

manhattan_distance = 0

for ss in range(len(stars)):
    for tt in range(ss + 1, len(stars)):
        s = stars[ss]
        t = stars[tt]
        v = abs(s[0] - t[0]) + abs(s[1] - t[1])
        manhattan_distance += v

print(manhattan_distance)
