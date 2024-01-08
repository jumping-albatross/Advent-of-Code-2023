# Day 16 Part 2
# Note: \ (backslash) has been replaced with ` (backtick) in raw data
import time

t1 = time.time()

raw = """.|...`....
|.-.`.....
.....|-...
........|.
..........
.........`
..../.``..
.-.-/..|..
.|....-|.`
..//.|....""".split("\n")

with open("day_16.dat") as f:
    raw = f.read().split("\n")

R = len(raw)
C = len(raw[0])

# The starting tiles grid with with spaces and mirrors

TILES = raw


def launch_beam(start_beam):
    """Simulate the full route one beam of light takes. A beam is (dx, dy, x, y)."""

    beams = {start_beam}

    # set of visited tiles and beams
    visited = set()

    while len(beams) > 0:
        new_beams = set()
        for beam in beams:
            # A beam is (dx, dy, x, y)
            dx, dy, x, y = beam
            x, y = x + dx, y + dy
            
            if 0 <= x < C and 0 <= y < R:
                tile = TILES[y][x]
            else:
                continue  # skip this beam. It leaves the grid of tiles
 
            if tile == "/":
                # 1a. reflect beam (/\)
                dx, dy = -dy, -dx
                new_beams.add((dx, dy, x, y))
            elif tile == "`":
                # 1b. reflect beam (/\)
                dx, dy = dy, dx
                new_beams.add((dx, dy, x, y))
            elif tile == "-":
                if dy != 0:
                    # 2a. reflect and split beam (-|)
                    dx, dy = dy, dx
                    new_beams.add((dx, dy, x, y))
                    dx, dy = -dx, -dy
                    new_beams.add((dx, dy, x, y))
                else:
                    # 2b. continue forward (-|)
                    new_beams.add((dx, dy, x, y))
            elif tile == "|":
                if dx != 0:
                    # 2c. reflect and split beam (-|)
                    dx, dy = dy, dx
                    new_beams.add((dx, dy, x, y))
                    dx, dy = -dx, -dy
                    new_beams.add((dx, dy, x, y))
                else:
                    # 2b. continue forward (-|)
                    new_beams.add((dx, dy, x, y))
            else:
                # 2c. continue forward (.)
                new_beams.add((dx, dy, x, y))

        beams = set()

        for beam in new_beams:
            if beam not in visited:
                beams.add(beam)
                visited.add(beam)

    tiles_visited = set()

    for v in visited:
        tiles_visited.add((v[2:]))

    return len(tiles_visited)


most_energetic = -1 # x, y, tiles_energized

for x in range(C):
    dx = 0
    for y, dy in ((-1, 1), (R, -1)):
        energy = launch_beam((dx, dy, x, y))
        if energy > most_energetic:
            most_energetic = energy

for y in range(R):
    dy = 0
    for x, dx in ((-1, 1), (C, -1)):
        energy = launch_beam((dx, dy, x, y))
        if energy > most_energetic:
            most_energetic = energy

print(f"most_energetic = {most_energetic}")
print(time.time() - t1)