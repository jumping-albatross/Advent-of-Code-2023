# https://github.com/oloturia/AoC2023/blob/main/day21/part1.py

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

ROWS = len(grid)
COLS = len(grid[0])

start = (0, 1)
terminal = (ROWS - 1, COLS - 2)
print(f"{terminal = }")

# extract nodes_queue, edges and distances

edges = {}  # { node : [{node1, node2, distance)} }
nodes = {}
nodes_queue = {(start, (1, 0))}  # {(node, (dr, dc)}
nodes_visited = set()


def count_paths(p, deltas):
    r, c = p
    incoming_dr, incoming_dc = deltas
    paths_available = 0
    for dr, dc in zip((1, -1, 0, 0), (0, 0, 1, -1)):
        _r = r + dr
        _c = c + dc

        if (incoming_dr, incoming_dc) != (-dr, -dc) and 0 <= _r < ROWS and 0 <= _c < COLS and grid[_r][_c] != '#':
            paths_available += 1
    return paths_available


def add_edges_nodes(a, b, l):
    """a is start, b is stop, l is distance"""
    a, b = sorted([a, b])
    edges[(a, b)] = l

    if a in nodes:
        nodes[a].add(b)
    else:
        nodes[a] = {b}

    if b in nodes:
        nodes[b].add(a)
    else:
        nodes[b] = {a}


count = 0
while nodes_queue:
    count += 1

    p, (prev_dr, prev_dc) = nodes_queue.pop()
    nodes_visited.add((p, (prev_dr, prev_dc)))
    # when the node was pushed to the queue the next move's direction was included
    print(f"Round: {count}, {len(edges) = }, {len(nodes_queue) = }, {len(nodes_visited) = }, {p = }, {(prev_dr, prev_dc) = }")
    length = 1
    r = p[0] + prev_dr
    c = p[1] + prev_dc

    while count_paths((r, c), (prev_dr, prev_dc)) == 1 and (r, c) != terminal:
        for dr, dc in zip((1, -1, 0, 0), (0, 0, 1, -1)):
            _r = r + dr
            _c = c + dc

            if (-dr, -dc) != (prev_dr, prev_dc) and 0 <= _r < ROWS and 0 <= _c < COLS:
                cell = grid[_r][_c]
                if cell != '#':
                    length += 1
                    r, c = _r, _c
                    prev_dr, prev_dc = dr, dc
                    break

    if (r, c) == terminal:
        add_edges_nodes(p, terminal, length)
    else:
        cnt = count_paths((r, c), (prev_dr, prev_dc))
        if cnt == 2 or cnt == 3:
            add_edges_nodes(p, (r, c), length)
            for dr, dc in zip((1, -1, 0, 0), (0, 0, 1, -1)):
                _r = r + dr
                _c = c + dc

                if 0 <= _r < ROWS and 0 <= _c < COLS:
                    cell = grid[_r][_c]
                    if cell != '#' and ((r, c), (dr, dc)) not in nodes_visited:
                        nodes_queue.add(((r, c), (dr, dc)))
        elif cnt == 0:
            pass
        else:
            print(f"{(r, c) = }")
            raise Exception(f"{cnt} path(s) when 2 or 0 expected")

print('\nEdges found')
for edge in sorted(edges):
    print(f"{edge}")

print('\nNodes found')
for node in sorted(nodes):
    print(f"{node} : {nodes[node]}")
print()

print(f"{ROWS = }, {COLS = }")
print(f"{len(edges) = }, {len(nodes) = }")

for (r, c) in nodes:
    t = list(grid[r])
    t[c] = '█'
    grid[r] = ''.join(t)


print('\nLooking for longest edge...')

q = [[start]]
finished = []

while q:
    path = q.pop()
    for dest in nodes[path[-1]]:
        if dest not in path:
            p2 = path[:]
            p2.append(dest)
            if dest == terminal:
                finished.append(p2)
            else:
                q.append(p2)

m = 0
for f in finished:
    d = 0
    for i in range(len(f) - 1):
        v = tuple(sorted(tuple([f[i], f[i + 1]])))
        d += edges[v]
    # print(d)
    m = max(m, d)

print(len(finished))
print(f"This is it: {m}")
