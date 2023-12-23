from collections import deque

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
    with open('day_21.txt') as f:
        grid = f.read().strip().split('\n')

for i, row in enumerate(grid):
    if 'S' in row:
        start = (i, row.find('S'))
        grid[i] = row.replace('S', '.')
        break

q = deque()
q.append((STEPS, start))

plots_reached = set()
plots_walked = {}


counter = 0

while q:
    counter += 1
    steps_remaining, coord = q.pop()
    if (steps_remaining) % 2 == 0:
        plots_reached.add(coord)

    # if counter < 10:
    #     print(f"{coord = }")
    # if counter % 100000 == 0:
    #     print(f"{counter}, {steps_remaining = }, {coord = }, {len(q) = }")

    if steps_remaining > 0:
        steps_remaining -= 1
        r, c = coord
        for (dr, dc) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr = r + dr
            nc = c + dc

            if grid[nr][nc] == '.' and (nr, nc) not in plots_walked:
                q.append((steps_remaining, (nr, nc)))

    if coord in plots_walked:
        plots_walked[coord] += 1
    else:
        plots_walked[coord] = 1

grid_l = []
for g in grid:
    grid_l.append(list(g))

for (r, c) in plots_reached:
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

print(len(plots_reached))
print(f"{start = }")
if testing:
    print(f"{matches = }")

# 2925 too low
# 3186 too low
# 3666 is it https://github.com/stefanoandroni/advent-of-code/blob/master/2023/day-21/part-1/main.py
