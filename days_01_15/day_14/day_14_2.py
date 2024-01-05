import operator

testing = False

if testing:
    raw = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".strip().split("\n")
else:
    with open("data14.txt") as r:
        raw = r.read().strip().split("\n")

ROWS = len(raw)
COLS = len(raw[0])

rocks = []
for r in range(len(raw)):
    for c in range(len(raw[0])):
        if raw[r][c] != '.':
            rocks.append([r, c, raw[r][c]])


def show_rock_grid(expected=False):
    grid = [['.' for _ in range(len(raw[0]))] for _ in range(len(raw))]
    for rr, cc, vv in rocks:
        grid[rr][cc] = vv
    expected = """.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....""".split()
    load = 0
    for idx, g in enumerate(grid):
        line = ''.join(g)
        load += (ROWS - idx) * line.count('O')
        print(f"O: {line}")
        if expected:
            print(f"E: {expected[idx]}")
            print()
    print("Load:", load)

    return grid


def tilt(v, h):
    """v: -1 up/north, 1 down/south; h: -1 left/west, 1 right/east; h & v: 0 do nothing"""

    R, C = 0, 1

    final_edge = 0 if v + h == -1 else ROWS - 1

    if v != 0 and h == 0:
        # sort for vertical tilt
        rocks.sort(key=operator.itemgetter(C, R), reverse=v != -1)

        current_row = final_edge
        current_col = -1
        for idx in range(len(rocks)):
            r, c, val = rocks[idx]
            if current_col != c:  # reset the current row or col
                current_col = c
                current_row = final_edge
            if val == 'O':
                rocks[idx][R] = current_row
                current_row += 1 * -v  # swap for N/S
            elif val == '#':
                current_row = r + 1 * -v  # swap for N/S
    else:
        # sort for horizontal tilt
        rocks.sort(key=operator.itemgetter(R, C), reverse=h != -1)

        current_col = final_edge
        current_row = -1
        for idx in range(len(rocks)):
            r, c, val = rocks[idx]
            if current_row != r:  # reset the current row or col
                current_row = r
                current_col = final_edge
            if val == 'O':
                rocks[idx][C] = current_col
                current_col += 1 * -h  # swap for N/S
            elif val == '#':
                current_col = c + 1 * -h  # swap for N/S


def rock_hash(silent=True):
    v = ''
    for vv in rocks:
        if not silent:
            print(vv)
        v += str(vv)
    return v


def calc_load():
    load = 0
    for r, c, v in rocks:
        if v == 'O':
            load += ROWS - r
    return load


# determine the periodic layouts
# one cycle is four tilts, n>w>s>e
platform_layouts = {}
loads = []
for i in range(1, 10000):
    for ns, we in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
        tilt(ns, we)

    l = rock_hash()
    if l in platform_layouts:
        if platform_layouts[l] + 1 == 3:
            break
        loads.append(calc_load())
        platform_layouts[l] += 1
    else:
        platform_layouts[l] = 1

# eliminate the non-repeating layouts
offset = 0
for k in platform_layouts:
    if platform_layouts[k] == 1:
        offset += 1

period = len(platform_layouts) - offset
print(
    f"Part 2: {(1e9 - offset) % period = }, \nLoad after round 1e9 cycles = {loads[int((1e9 - offset) % period - 1)]}")
