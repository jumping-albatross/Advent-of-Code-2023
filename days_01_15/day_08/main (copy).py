is_testing = False
is_try_one = True
is_part_one = True


if is_testing:
    if is_try_one:
        raw = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''.split('\n')
        goal = 2
    else:
        raw = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''.split('\n')
        goal = 6
else:
    with open('data08.txt') as f:
        raw = f.read().split('\n')
    goal = 0

instructions = raw[0]
network_raw = raw[2:]

network = {}
for node in network_raw:
    origin = node[:3]
    dl = node[7:10]
    dr = node[12:15]
    network[origin] = {'L':dl, 'R':dr}

def end_search():
    current_node = 'AAA'
    steps = 0
    while True:
        for i in instructions:
            steps += 1
            current_node = network[current_node][i]
            if current_node == 'ZZZ':
                print(steps)
                return

end_search()