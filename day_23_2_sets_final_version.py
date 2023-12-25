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

# to do: convert the path to a set. Only the current tile needs to be tracked. Never revisit a tile.
paths = [[set(), start]]
paths_ended = []

count = 0
m = 0
while paths:
    count += 1
    # print(f"{count = }")

    s, p = paths.pop()
    if p == terminal:
        # print(p)
        m = max(m, len(s))
        print(f"{count:>10}, {len(paths):>10},  current: {len(s):>6},  max {m:>6}")

    # print(p)
    r, c = p

    num_chosen = 0
    for dr, dc in zip((1,-1, 0, 0), (0, 0, 1, -1)):
        _r = r + dr
        _c = c + dc
        if 0 <= _r < len(grid) and 0 <= _c < len(grid[0]):
            cell = grid[_r][_c]
            if cell != '#' and (_r, _c) not in s:
                num_chosen += 1

    if num_chosen != 1:
        for dr, dc in zip((1,-1, 0, 0), (0, 0, 1, -1)):
            _r = r + dr
            _c = c + dc

            if 0 <= _r < len(grid) and 0 <= _c < len(grid[0]):
                cell = grid[_r][_c]
                if cell != '#':
                    if 0 <= _r < len(grid) and 0 <= _c < len(grid[0]) and cell != '#':
                        if (cell == '.'):
                                if (_r, _c) not in s:
                                    s2 = s.copy()
                                    s2.add(p)
                                    paths.append((s2, (_r, _c)))
    else:
        while num_chosen == 1:
            for dr, dc in zip((1,-1, 0, 0), (0, 0, 1, -1)):
                _r = r + dr
                _c = c + dc

                if 0 <= _r < len(grid) and 0 <= _c < len(grid[0]):
                    cell = grid[_r][_c]
                    if cell != '#':
                        if 0 <= _r < len(grid) and 0 <= _c < len(grid[0]) and cell != '#':
                            if (cell == '.'):
                                    if (_r, _c) not in s:
                                        s.add(p)
                                        p = _r, _c
            num_chosen = 0
            for dr, dc in zip((1,-1, 0, 0), (0, 0, 1, -1)):
                _r = r + dr
                _c = c + dc
                if 0 <= _r < len(grid) and 0 <= _c < len(grid[0]):
                    cell = grid[_r][_c]
                    if cell != '#' and (_r, _c) not in s:
                        num_chosen += 1
            if num_chosen != 1:
                paths.append((s, p))

for p in paths_ended:
    if p[-1] == terminal:
     print("p,'\n',len(p)")

print(f"{len(grid) = }, {len(grid[0]) = }")
print(f"{len(paths_ended)}")
print(f"{m = }")

# 5890 too low
# 5938 too low

