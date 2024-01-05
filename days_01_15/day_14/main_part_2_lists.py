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
    print("""TODO
    dentist
    optometrist
    letter to doc
    note to aunluk
    sms DS
    """)

ROWS = len(raw)
COLS = len(raw[0])

rocks = []
for r in range(len(raw)):
    for c in range(len(raw[0])):
        if raw[r][c] != '.':
            rocks.append([r, c, raw[r][c]])


#
# for r in rocks:
#     print(r)
def show_rock_grid(expected=True):
    grid = [['.' for _ in range(len(raw[0]))] for _ in range(len(raw))]
    for rr, cc, vv in rocks:
        grid[rr][cc] = vv
    sample = """.....#....
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
    for i, g in enumerate(grid):
        line = ''.join(g)
        load += (ROWS - i) * line.count('O')
        print(f"O: {line}")
        if expected:
            print(f"E: {sample[i]}")
            print()
    print("Load:", load)

    return grid


def tilt(v, h):
    '''v==-1 up, 0 nothing, 1 down
    h==-1 left, 0 nothin, 1 right'''

    R, C = 0, 1

    final_edge = 0 if v + h == -1 else ROWS - 1

    if v != 0 and h == 0:
        # sort for vertical tilt
        rocks.sort(key=operator.itemgetter(C, R), reverse=v != -1)
        # print(rocks)
        # print("vertical")
        # exit()

        current_row = final_edge
        current_col = -1
        for idx in range(len(rocks)):
            r, c, val = rocks[idx]
            if current_col != c:  # reset the current row or col
                current_col = c
                current_row = final_edge
                # print(final_edge, c, rocks[idx], R, C)
            if val == 'O':
                # print(rocks[idx], ">", end ="")
                rocks[idx][R] = current_row
                current_row += 1 * -v  # swap for N/S
                # print(rocks[idx], current_row)
            elif val == '#':
                current_row = r + 1 * -v  # swap for N/S
        # show_rock_grid(expected=False)
        # exit()
    else:
        # sort for horizontal tilt
        rocks.sort(key=operator.itemgetter(R, C), reverse=h != -1)
        # print(rocks)
        # print("horizontal")
        # exit()

        current_col = final_edge
        current_row = -1
        for idx in range(len(rocks)):
            r, c, val = rocks[idx]
            if current_row != r:  # reset the current row or col
                current_row = r
                current_col = final_edge
                # print(final_edge, r, rocks[idx], R, C)
            if val == 'O':
                # print(rocks[idx], ">", end ="")
                rocks[idx][C] = current_col
                current_col += 1 * -h  # swap for N/S
                # print(rocks[idx], current_col)
            elif val == '#':
                current_col = c + 1 * -h  # swap for N/S
        # show_rock_grid(expected=False)
        # exit()


# changes = -1
# while changes != None:
# one cycle is four tilts, n>w>s>e
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


s = {}
loads = []
for i in range(1, 10000):
    for ns, we in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
        tilt(ns, we)

    l = rock_hash()
    loadd = calc_load()
    if l in s:
        loads.append(loadd)
        if s[l] + 1 == 3:
            break
        s[l] += 1
        # print(f"{i = }, {s[l] = } {len(s) = }, {loadd = }{'' if loadd != 64 else '***'}")
    else:
        s[l] = 1
        # print(f"{i = }, {s[l] = } {len(s) = }, {loadd = }{'' if loadd != 64 else '***'}")

to_pop = []
for k in s:
    if s[k] == 1:
        to_pop.append(k)

offset = len(to_pop)
for pop in to_pop:
    s.pop(pop)

print(f"Part 2: {(1e9 - offset) % len(s) = }, \nLoad after round 1e9 = {loads[int((1e9 - offset) % len(s) - 1)]}")
