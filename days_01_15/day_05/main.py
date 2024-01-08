raw = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

with open('day_05.dat') as f:
    raw = f.read().strip()

# Stage 1 Prepare data
raw = raw.split(':')[1:]
raw[-1] += '\n\n'
seeds = raw[0].split()[:-2]
seed_ranges = seeds[:]

raw_maps = [m.split('\n')[1:-2] for m in raw[1:]]

maps = []
for raw_map in raw_maps:
    individual_maps = []
    for _imap in raw_map:
        individual_maps.append(list(map(int, _imap.split())))
    individual_maps.sort(key=lambda x: x[1])  # reverse sort order on source

    maps.append(individual_maps)

# Part 1:
seeds = [[int(x)] for x in seeds]

# Part 1:  Stage 2 Analyse data

for individual_maps in maps:
    for idx, seed in enumerate(seeds):
        for _m in individual_maps:
            DEST = 0
            SRC = 1
            RNG = 2
            if _m[SRC] <= seed[0] <= _m[SRC] + _m[RNG]:
                # found map
                seeds[idx] = [seed[0] - _m[SRC] + _m[DEST]] + seed
                break
# Stage 3 Show output
print('Expected lowest location = 35')
seeds.sort()
print("Part 1 =", seeds[0][0])

# Part 2

# Stage 1 Prepare seed ranges

seeds = []
for idx in range(0, len(seed_ranges), 2):
    # SRC, RNG
    seeds += [(int(seed_ranges[idx]), int(seed_ranges[idx + 1]))]
DEST = 0
SRC = 1
RNG = 2

# Stage 2 Map seed ranges


def map_range(the_map, start, end):
    '''Given the map, the start and end coordinates return new start and range.
    Start and End MUST fall within the map range'''

    d = the_map[0]
    s = the_map[1]
    the_map[2]

    start_destination = d + start - s
    range_destination = end - start + 1  # good
    return (start_destination, range_destination)


# New ROUND
for _round in maps:

    # Process each and every seed
    for idx, seed in enumerate(seeds):

        # Try each map
        for _m in _round:

            start_map = _m[SRC]
            end_map = _m[SRC] + _m[RNG] - 1

            start_seed = seed[0]
            end_seed = seed[0] + seed[1] - 1

            if (start_seed <= end_map) and (end_seed >= start_map):
                # Found overlap
                if start_seed < start_map:
                    append_seed = (start_seed, start_map - start_seed)  # good
                    seeds.append(append_seed)

                    if end_seed <= end_map:
                        seeds[idx] = map_range(_m, start_map, end_seed)  # good
                        break
                    else:
                        seeds[idx] = map_range(_m, start_map, end_map)
                        append_seed = (end_map + 1, end_seed - end_map)  #good
                        seeds.append(append_seed)
                        break
                else:
                    # Does the map cover the whole seed range?
                    if end_seed <= end_map:
                        new_seed = map_range(_m, start_seed, end_seed)  # good
                        seeds[idx] = new_seed
                        break
                    else:
                        # Seed range ends beyond end of map range.
                        seeds[idx] = map_range(_m, start_seed, end_map)  # good
                        # append the excess to the seed ranges

                        append_seed = (end_map + 1, end_seed - end_map)  # good
                        seeds.append(append_seed)
                        break

# Stage 3 Show output
print('Expected lowest location = 46')
seeds.sort()
print(seeds[0][0])
