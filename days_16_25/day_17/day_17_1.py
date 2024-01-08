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

with open('day_17.dat') as f:
    grid = f.read().split('\n')
R = len(grid)
C = len(grid[0])

queue = []
visited = {} # key = r, c, last_direction, longest_run : value = cost
# last direction: -99 is nothing; otherwise 0-3 or (0, 1), (1, 0), (0, -1), (-1, 0)
start = (0, 0, 0, -99, 0) # cost, r, c, last_direction, longest_run

queue = [start]

heapq.heapify(queue)

while queue:
    cost, r, c, last_direction, longest_run = heapq.heappop(queue)

    if (r, c, last_direction, longest_run) in visited:
        continue # skip this round. Been here before with a lower cost
    else:
        visited[(r, c, last_direction, longest_run)] = cost

    for idx, (dx, dy) in enumerate([(0, 1), (1, 0), (0, -1), (-1, 0)]):
        if 0 <= r + dy < R and 0 <= c + dx < C:
            v = int(grid[r + dy][c + dx])

            if last_direction == (idx + 2) % 4:
                # print(f"{len(queue) = }     {len(visited) = }")
                continue
            
            if last_direction == idx:
                if longest_run < 3:
                    new_longest_run = longest_run + 1
                else:
                    continue # skip following this path
            else:
                new_longest_run = 1
                
                
            heapq.heappush(queue, (cost + v, r + dy, c + dx, idx, new_longest_run))

for v in visited:
    if v[0] == R-1 and v[1] == C-1:
        print(f"{visited[v] = }")