#https://github.com/oloturia/AoC2023/blob/main/day21/part1.py
#
testing = False

if testing:
    grid = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
""".strip().split('\n')
else:
    with open('day23.txt') as f:
        grid = f.read().strip().split('\n')

start = (0, 1)
terminal = (len(grid) - 1, len(grid[0]) - 2)
print(f"{terminal = }")

paths = [[start]]
paths_ended = []

count = 0
m = 0
while paths:
    count += 1
    # print(f"{count = }")

    p = paths.pop()
    if p[-1] == terminal:
        # print(p)
        print(len(p) - 1)
        m = max(m, len(p) - 1)

    # print(p)
    r, c = p[-1]

    for dr, dc in zip((1,-1, 0, 0), (0, 0, 1, -1)):
        _r = r + dr
        _c = c + dc

        # if (_r, _c) == terminal:
        #     print(f"{r, c = }, {terminal = }")

        if 0 <= _r < len(grid) and 0 <= _c < len(grid[0]):
            cell = grid[_r][_c]
            if cell != '#':
                if 0 <= _r < len(grid) and 0 <= _c < len(grid[0]) and cell != '#':
                    if (cell == '>' and _r == r and _c > c) or (cell == 'v' and _r > r and _c == c) or (cell == '.'):
                        if (_r, _c) not in p:
                            np = p[:]
                            np.append((_r, _c))
                            paths.append(np)

for p in paths_ended:
    if p[-1] == terminal:
     print("p,'\n',len(p)")

print(f"{len(grid) = }, {len(grid[0]) = }")
print(f"{len(paths_ended)}")
print(f"{m = }")
