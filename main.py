testing = False

if testing:
    raw = '''.....
.S-7.
.|.|.
.L-J.
.....'''.strip().split('\n')
else:
    with open('data10.txt') as f:
        raw = f.read().strip().split('\n')

grid = raw

current = [0, 0]
start = [0, 0]
for r, line in enumerate(grid):
    for c, v in enumerate(line):
        if v == 'S':
            current = [r, c]
            start = [r, c]


def find_exit(previous, current):
    '''
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there
      is a pipe on this tile, but your sketch doesn't
      show what shape the pipe has.'''

    # destination r, c; acceptable src pipe, dest pipe
    CARDINAL = (((-1,  0), '|LJS', '|7FS'), 
                (( 1,  0), '|7FS', '|LJS'), 
                (( 0, -1), '-J7S', '-LFS'), 
                (( 0,  1), '-LFS', '-J7S'))
    ROW = 0
    COL = 1
    
    for delta, src, dest in CARDINAL:
        rd = current[ROW] + delta[ROW]
        cd = current[COL] + delta[COL]
        r = current[ROW]
        c = current[COL]
        try:
            if grid[r][c] in src and grid[rd][cd] in dest and [rd, cd] != previous:
                return [rd, cd]
        except:
            print('Except', rd,cd)
            raise Exception("Why did we get here?")

    raise Exception(f"Ooops. Find exit failed with {previous}, {current}")

path = [start]
current = find_exit(current, current)
path.append(current)

while current != start:
    current = find_exit(path[-2], current)
    path.append(current)
        
print("Part 1", (len(path) - 1) // 2)


# Search for contained squares
start_inside = (41, 14)
start_outside = (41, 12)
start_pipe = (41, 13)
start_idx = path.index(list(start_pipe))

INSIDE_SYMBOL = '⬤' #'\u2B24'
PATH_SYMBOL = '█'

matrix = [list(line) for line in grid]

new_edge = [[path[start_idx]]]
for idx in range(start_idx, start_idx + len(path), 1):
    # NEXT MOVE
    # destination r, c; acceptable src pipe, dest pipe
    current = path[idx % len(path)]
    next = path[(idx + 1) % len(path)]
 
    src_r = current[0]
    src_c = current[1]
    dest_r = next[0]
    dest_c = next[1]
    



# Create visualization
for c in path:
    matrix[c[0]][c[1]] = PATH_SYMBOL

with open('day_10.grid', 'w') as r:
    for line in matrix:
        r.write(''.join(line) + '\n')
