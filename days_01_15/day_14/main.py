raw = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".split("\n")

# with open("data14.txt") as r:
#     raw = r.read().split("\n")

platform = [list(x) for x in raw]


def tilt(v, h):
    '''v==-1 up, 0 nothing, 1 down
    h==-1 left, 0 nothin, 1 right'''
    changes = 0

    if v == -1:
        for r in range(1, len(platform)):
            for c in range(0, len(platform[0])):
                if platform[r][c] == 'O':
                    for move_r in range(r - 1, 0 - 1, -1):
                        if platform[move_r][c] == '.':
                            platform[move_r + 1][c] = '.'
                            platform[move_r][c] = 'O'
                            changes += 1
                        else:
                            break
    return changes


changes = -1
while changes != 0:
    changes = tilt(-1, 0)
    print(changes)

print("Part 1:\n")

# for r in platform:
#     print(''.join(r))

load = 0
pl = len(platform)
for i, line in enumerate(platform):
    load += (pl - i) * ''.join(line).count('O')

print()
print("Part 1 load", load)
