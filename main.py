#https://github.com/oloturia/AoC2023/blob/main/day21/part1.py
#
testing = True

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
"""
else:
    with open('day23.txt') as f:
        grid = f.read()

grid = grid.strip()
for ch in '^v<>':
    grid = grid.replace(ch, '.')

grid = grid.split('\n')

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
        m = max(m, len(p) - 1)
        print(f"current: {len(p) - 1:>6}, max {m:>6}")

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
                    if (cell == '.'):
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

# 5890 too low
# 5938 too low

