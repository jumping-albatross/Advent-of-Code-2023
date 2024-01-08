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
    goal = 2
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
active_nodes = set()

# add all nodes ending in A to current_nodes
for start_node in network:
    if start_node[2] == 'A':
        active_nodes.add(start_node)
print(48, active_nodes)
steps = 1

#experiment
paths = {}
for node in active_nodes:
    paths[node] = 0

while True:
    for i in instructions:
        new_nodes = set()
        while len(active_nodes) > 0:
            start_node = active_nodes.pop()
            dest_node = network[start_node][i]
            new_nodes.add(dest_node)
        else:
            active_nodes = new_nodes
            # all active nodes processed
            # check to see if all nodes end in Z
            for start_node in active_nodes:
                if start_node[-1] != "Z":
                    break
            else:
                print("Final answer? ", steps)
                6 / 0
            steps += 1
            if steps % 100000 == 0:
                print(steps, active_nodes)
