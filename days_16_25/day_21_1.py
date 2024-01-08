#https://github.com/oloturia/AoC2023/blob/main/day21/part1.py
#
testing = False

if testing:
    STEPS = 6
    grid = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".split('\n')
else:
    STEPS = 64
    with open('day_21.dat') as f:
        grid = f.read().strip().split('\n')

for i, row in enumerate(grid):
    if 'S' in row:
        start = (i, row.find('S'))
        grid[i] = row.replace('S', '.')
        break

q = set()
q.add(start)

for i in range(STEPS):
    qq = set()
    for (r, c) in q:
        for (dr, dc) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr = r + dr
            nc = c + dc
            if grid[nr][nc] == '.':
                qq.add((nr, nc))
    q = qq

grid_l = []
for g in grid:
    grid_l.append(list(g))

for (r, c) in q:
    grid_l[r][c] = "O"

print(grid_l[start[0]][start[1]])

check = """...........
.....###.#.
.###.##.O#.
.O#O#O.O#..
O.O.#.#.O..
.##O.■####.
.##.O#O..#.
.O.O.O.##..
.##.#.####.
.##O.##.##.
...........""".split('\n')
matches = True

grid_l[start[0]][start[1]] = "■"
for r, line in enumerate(grid_l):
    if abs(r - start[0]) < 6:
        print(''.join(line))
        if testing:
            matches = matches and ''.join(line) == check[r]

print(f"{len(q) = }")
print(f"{start = }")
if testing:
    print(f"{matches = }")

# 2925 too low
# 3186 too low
# 3666 is it https://github.com/stefanoandroni/advent-of-code/blob/master/2023/day-21/part-1/main.py
