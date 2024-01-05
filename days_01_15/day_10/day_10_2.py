# https://www.mathed.page/geoboard/grid-paper/index.html
# https://nbviewer.org/github/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo%27s_Advent_of_Code_2023.ipynb

ROW = 0
COL = 1

testing = False

if testing:
    raw = '''...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
'''.strip().split('\n')
    part_1 = 23
else:
    with open('data10.txt') as f:
        raw = f.read().strip().split('\n')
    part_1 = 6890

grid = raw

for r, line in enumerate(grid):
    for c, v in enumerate(line):
        if v == 'S':
            current = start = [r, c]


def trace_path(start):
    def part_1_find_exit(previous, current):
        """
        | is a vertical pipe connecting north and south.
        - is a horizontal pipe connecting east and west.
        L is a 90-degree bend connecting north and east.
        J is a 90-degree bend connecting north and west.
        7 is a 90-degree bend connecting south and west.
        F is a 90-degree bend connecting south and east.
        . is ground; there is no pipe in this tile.
        S is the starting position of the animal; there
          is a pipe on this tile, but your sketch doesn't
          show what shape the pipe has."""

        # destination r, c; acceptable src pipe, dest pipe
        CARDINAL = (((-1, 0), '|LJS', '|7FS'),
                    ((1, 0), '|7FS', '|LJS'),
                    ((0, -1), '-J7S', '-LFS'),
                    ((0, 1), '-LFS', '-J7S'))

        for delta, src, dest in CARDINAL:
            dr = current[ROW] + delta[ROW]
            dc = current[COL] + delta[COL]
            r = current[ROW]
            c = current[COL]

            if grid[r][c] in src and grid[dr][dc] in dest and [dr, dc] != previous:
                return [dr, dc]

        raise Exception(f"Oops. Find exit failed with {previous}, {current}")

    _path = [start, part_1_find_exit(start, start)]

    while _path[-1] != start:
        _path.append(part_1_find_exit(_path[-2], _path[-1]))

    return _path


# noinspection PyUnboundLocalVariable
path = trace_path(start)

print(f"Part 1: {(len(path) - 1) // 2 = }, (expected {part_1})")

assert (len(path) - 1) // 2 == part_1

print("Part 2")

FILL_SYMBOL = '⬤'  # '\u2B24'
PATH_SYMBOL = '█'


def write_path_visualization():
    start_pipe = start
    start_idx = path.index(list(start_pipe))

    matrix = [list(line) for line in grid]

    for (r, c) in path:
        matrix[r][c] = PATH_SYMBOL

    with open('day_10.grid', 'w') as r:
        for line in matrix:
            r.write(''.join(line) + '\n')


# Action: Search for contained squares
# write_path_visualization()


def empty_grid(rows, cols, resize):
    return [['.'] * cols * resize for _ in range(rows * resize)]


# TODO
# 1 create empty grid of at least 3x3 or larger
SCALE = 3

grid_scaled = empty_grid(len(grid) + 1, len(grid[0]) + 1, SCALE)  # add 1 to eliminate cut-off external fjords


# 2 draw outline of path on this much larger grid
def add_path_to_scaled_grid(_grid, _path, resize):
    """Draws the given path with a width of two on a resize times scaled grid"""
    for i in range(len(_path)):
        cr, cc = _path[i]
        # adding 1 now avoids (a) wrap-around errors and (b) including fjords at the edges as interior area
        cr, cc = cr + 1, cc + 1
        cr, cc = cr * resize, cc * resize

        nr, nc = _path[(i + 1) % len(_path)]
        nr, nc = nr + 1, nc + 1

        nr, nc = nr * resize, nc * resize

        a, b = min(cr, nr) - 1, max(cr, nr) + 1
        u, v = min(cc, nc) - 1, max(cc, nc) + 1

        for r in range(a, b):
            for c in range(u, v):
                _grid[r][c] = PATH_SYMBOL


add_path_to_scaled_grid(grid_scaled, path, SCALE)

# 3 flood fill starting at 0,0
nodes_filled = 0


def flood_fill_scaled_grid(__grid, r, c, old_colour, new_colour, offset_r=2, offset_c=2):
    """Accepts grid as 2-d array, starting row and column as r, c,
    and the previous colour and new colour values"""
    queue = []
    R = len(__grid)
    C = len(__grid[0])

    def colour_pixel(__r, __c):
        global nodes_filled

        if __grid[__r][__c] == new_colour:
            raise Exception(f"Unexpected. Pixel already filled in with {new_colour}")

        __grid[__r][__c] = new_colour

        tr = (__r) / SCALE - offset_r
        tc = (__c) / SCALE - offset_c

        if tr == int(tr) and tc == int(tc):  # only accept nodes
            if 0 <= tr < len(grid) and 0 <= tc < len(grid[0]):
                nodes_filled += 1
                __grid[__r][__c] = FILL_SYMBOL

    # Append the position of starting
    # pixel of the component
    queue.append([r * SCALE + offset_r, c * SCALE + offset_c])

    # Color the pixel with the new color
    colour_pixel(r * SCALE + offset_r, c * SCALE + offset_c)

    # While the queue is not empty
    while queue:

        # Dequeue the front node
        curr_pixel = queue.pop()

        pos_r, pos_c = curr_pixel

        # Check if the adjacent
        # pixels are valid
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if 0 <= pos_r + dr < R and 0 <= pos_c + dc < C:
                if __grid[pos_r + dr][pos_c + dc] == old_colour:
                    # color and enqueue
                    colour_pixel(pos_r + dr, pos_c + dc)
                    queue.append([pos_r + dr, pos_c + dc])


if not testing:
    flood_fill_scaled_grid(grid_scaled, 72, 71, '.', 'O')
else:
    flood_fill_scaled_grid(grid_scaled, 0, 0, '.', 'O')

# 4 Troubleshooting
for i, g in enumerate(grid_scaled):
    # if i > 5:
    #     break
    # for j, h in enumerate(grid_scaled[i]):
    #     if (i - 2) % SCALE == 0 and (j - 2) % SCALE == 0:
    #         grid_scaled[i][j] = FILL_SYMBOL
    print(f"{(i - 2) // SCALE:>3}" + "".join(g))

print("   ", end="")
for i in range(0, 400):
    print(f"{(i - 2) // SCALE % 10}", end="")

print()
print("   ", end="")
for i in range(0, 400, 10):
    print(f"{(i - 2) // SCALE:<10}", end="")

print()
print()
h, w = len(grid), len(grid[0])
print(f"{len(grid) = } x {len(grid[0]) = } = {h * w}")
print(f"{len(path) = }")
print(f"{len(grid) * len(grid[0]) - len(path) = }")

# 4 count nodes at a multiple of SCALE which haven't been filled
print(f"{nodes_filled = }")
