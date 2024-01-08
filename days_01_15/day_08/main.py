from math import lcm

a = open('day_08.dat').read().split('\n\n')
d = a[0]

dirs = {b[:3]: (b[7:10], b[12:15]) for b in a[1].split('\n')}
stepNum = 0
curSteps = [i for i in dirs if i[2] == 'A']
distances = []

while len(distances) < 6:
    for i in range(len(curSteps)):
        if curSteps[i][2] == 'Z':
            distances.append(stepNum)
        idx = 0 if d[stepNum % len(d)] == 'L' else 1
        curSteps[i] = dirs[curSteps[i]][idx]
    stepNum += 1

print(lcm(*distances))

is_testing = False

if is_testing:
    raw = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''.split('\n')
else:
    with open('day_08.dat') as f:
        raw = f.read().split('\n')
    goal = 0

instructions = raw[0]
network_raw = raw[2:]

network = {}
for node in network_raw:
    origin = node[:3]
    dl = node[7:10]
    dr = node[12:15]
    network[origin] = {'L': dl, 'R': dr}

# def end_search():
active_nodes = []

# add all nodes ending in A to current_nodes
for start_node in network:
    if start_node[2] == 'A':
        active_nodes.append([start_node, start_node])
print(48, active_nodes)
steps = 1

#experiment
path_lengths = {}
for node in active_nodes:
    path_lengths[node[0]] = 0


def part_two():
    global steps
    while True:
        for i in instructions:
            for node in active_nodes:
                start_node = node[1]
                dest_node = network[start_node][i]
                node[1] = dest_node

                if dest_node[-1] == 'Z' and path_lengths[node[0]] == 0:
                    path_lengths[node[0]] = steps
                    print("*" * 20)
                    print(node, path_lengths[node[0]])
            else:
                # all active nodes processed
                # check to see if all cycle lengths found
                if 0 not in path_lengths.values():
                    print("\nWOOOHOO\n")
                    v = lcm(*path_lengths.values())
                    print(f"Final answer is {v}")
                    return v
                steps += 1


part_two()
