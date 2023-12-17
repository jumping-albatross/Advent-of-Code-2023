# Advent of Code 2023—Day 17. (n.d.). Retrieved 17 December 2023,
# from https://www.youtube.com/watch?v=jcZw1jRkUDE

import heapq

grid = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".split('\n')

# with open('data17.txt') as f:
#     grid = f.read().split('\n')

R = len(grid)
C = len(grid[0])

queue = []
visited = {}  # key = r, c, last_direction, longest_run : value = cost
# last direction: -99 is nothing; otherwise 0-3 or (0, 1), (1, 0), (0, -1), (-1, 0)
start = (0, 0, 0, -99, 0)  # cost, r, c, last_direction, longest_run

queue = [start]

heapq.heapify(queue)

while queue:
    cost, r, c, last_direction, longest_run = heapq.heappop(queue)

    if (r, c, last_direction, longest_run) in visited:
        continue  # skip this round. Been here before with a lower cost

    for idx, (dx, dy) in enumerate([(0, 1), (1, 0), (0, -1), (-1, 0)]):
        if 0 <= r + dy < R and 0 <= c + dx < C:
            v = int(grid[r + dy][c + dx])

            if last_direction == (idx + 2) % 4:
                # print(f"{len(queue) = }     {len(visited) = }")
                continue

            if last_direction != idx and longest_run < 4 and last_direction != -99:
                continue

            if last_direction == idx:
                if longest_run < 10:
                    new_longest_run = longest_run + 1
                else:
                    continue  # skip following this path
            else:
                new_longest_run = 1

            heapq.heappush(queue,
                           (cost + v, r + dy, c + dx, idx, new_longest_run))

            visited[(r, c, last_direction, longest_run)] = cost

costs = {(R - 1, C - 1): 99999999999}
for v in visited:
    if v[0] == R - 1 and v[1] == C - 1:
        print(f"{visited[v] = }")
        costs[(R - 1, C - 1)] = min(costs[(R - 1, C - 1)], visited[v])
    r, c = v[:2]
    if (r, c) in costs:
        costs[(r, c)] = min(costs[(r, c)], visited[v])
    else:
        costs[(r, c)] = visited[v]

reversed_path = [(R - 1, C - 1)]

while reversed_path[-1] != (0, 0):
    r, c = reversed_path[-1]
    min_tile = (999999,(999999,999999))
    for (dr, dc) in ((0,1), (1,0), (0,-1),(-1,0)):
        nr, nc = r + dr, c + dc
        try:
            min_tile = min(min_tile, (costs[(nr, nc)],(nr,nc)))
        except:
            "oops I did it again. Nothing to see. Move on."
    if min_tile == (999999,(999999,999999)):
        raise Exception("Ooops. No minimum tiles found")
    reversed_path.append((min_tile[1]))

print()
print(f"{costs[(R - 1, C - 1)] = }")
print(f"{len(visited) = }")

# {(12, 7, 0, 9) : 194}

with open('day17.path', 'w') as f:
    for v in visited:
        f.write(f"{{{str(v)} : {visited[v]}}}")
        f.write('\n')

print()
print("WARNING: This is NOT the correct path per the rules")
print("         Chances are it's '"'just'"' modified dijkstra's" )
illustration = [['.' for _ in range(C)] for _ in range(R)]
for (r, c) in reversed_path:
    illustration[r][c] = "*"
for i in illustration:
    print(''.join(i))