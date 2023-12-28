# day 25
# https://www.reddit.com/r/adventofcode/comments/18qbsxs/comment/kf12xgf/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# https://python-course.eu/applications-python/graphs-python.php
# https://www.reddit.com/r/adventofcode/comments/18qbsxs/comment/keuafrl/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# https://www.reddit.com/r/adventofcode/comments/18qbsxs/comment/kf94vru/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

import random
from time import time, asctime

print(f"Starting at {asctime()}...\n")
testing = False

if testing:
    raw_connections = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""
else:
    with open('day25.txt') as f:
        raw_connections = f.read()

connections = raw_connections.strip().splitlines()
nodes = {}


def add_node(nodes, n1, n2):
    if n1 not in nodes:
        nodes[n1] = {n2}
    else:
        nodes[n1].add(n2)


# create the graph
for line in connections:
    node, neighbours = line.split(': ')
    neighbours = neighbours.split()
    add_node(nodes, node, neighbours[0])

    for _n in neighbours[1:]:
        nodes[node].add(_n)

    for _n in neighbours:
        add_node(nodes, _n, node)


def cut_edges(edges=[('fch', 'fvh'), ('jbz', 'sqh'), ('nvg', 'vfj')]):
# cut the nodes
    for (c1, c2) in edges:
        nodes[c1].remove(c2)
        nodes[c2].remove(c1)

def find_random_path(start_vertex, end_vertex, path=None):
    """ find a path from start_vertex to end_vertex
        in graph """
    if path == None:  # TO DO conditional seems redundant
        path = []
    graph = nodes
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return path
    if start_vertex not in graph:
        return None

    neighbours = list(graph[start_vertex])
    random.shuffle(neighbours)
    for vertex in neighbours:
        if vertex not in path:
            extended_path = find_random_path(vertex, end_vertex, path)
            if extended_path:
                return extended_path
    return None


def find_random_path_iterate(start_vertex, end_vertex):
    """ iteratively find a path from start_vertex to end_vertex
        in graph """
    stack = [(start_vertex, [start_vertex])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex == end_vertex:
            return path
        neighbours = list(nodes[vertex])
        random.shuffle(neighbours)
        for neighbour in neighbours:
            if neighbour not in path:
                stack.append((neighbour, path + [neighbour]))
                break
    return None


def find_path(start_vertex, end_vertex, path=None):
    """ find a path from start_vertex to end_vertex
        in graph """
    if path == None:  # TO DO conditional seems redundant
        path = []
    graph = nodes
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return path
    if start_vertex not in graph:
        return None
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_path = find_path(vertex, end_vertex, path)
            if extended_path:
                return extended_path
    return None


node_frequencies = {}

rounds = 0
k1, k2 = list(nodes.keys()), list(nodes.keys())
sz = len(k1)


def return_edges(path):
    e = set()
    for i in range(len(path) - 1):
        e.add(tuple(sorted([path[i], path[i + 1]])))
    return e


has_cut = False
if not has_cut:
    # find nodes to cut
    for i in range(25):
        random.shuffle(k1)
        random.shuffle(k2)
        for node_0 in zip(k1[:sz], k2[:sz]):
            rounds += 1
            pt = find_random_path_iterate(node_0[0], node_0[1])
            if pt != None:
                for n in return_edges(pt):
                    if n in node_frequencies:
                        node_frequencies[n] += 1
                    else:
                        node_frequencies[n] = 1

    print(sorted(list(node_frequencies.items()), key=lambda x: x[1])[-10:])

    s1 = []
    for (x, _) in sorted(list(node_frequencies.items()), key=lambda x: x[1])[-3:]:
        s1.append(x)

    print('Testing: ', sorted([('hfx', 'pzl'), ('bvb', 'cmg'), ('jqt', 'nvd')]))
    print('         ', sorted(s1))
else:
    set1 = set()
    founder1 = 'fch'
    set2 = set()
    founder2 = 'fvh'
    t1 = time()
    while len(set1) + len(set2) - len(nodes.keys()):
        for founder_n, set_n, set_other in zip([founder1, founder2], [set1, set2], [set2, set1]):
            for i in list(nodes.keys()):
                if i in set_other or i in set_n:
                    break
                pt = find_random_path_iterate(i, founder_n)
                if pt != None:
                    set_n.add(i)
                    break
        print(f"{len(nodes.keys()) = }")
        print(f"{len(set1) = }")
        print(f"{len(set2) = }")
        print(f"{len(set1) + len(set2) - len(nodes.keys()) = }")
        print(f"{len(set1) * len(set2) = }")
        print()
    print(time() - t1)
