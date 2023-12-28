# day 25
# https://www.reddit.com/r/adventofcode/comments/18qbsxs/comment/kf12xgf/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# https://python-course.eu/applications-python/graphs-python.php
# https://www.reddit.com/r/adventofcode/comments/18qbsxs/comment/keuafrl/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

The cut portion works well.

Finding the edges to cut is less reliable and fails sometimes (random chance)

import random
from time import time

testing = False
has_cut = True

if testing:
    key_edges = (('hfx', 'pzl'), ('bvb', 'cmg'), ('jqt', 'nvd'))
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
    key_edges = (('fch', 'fvh'), ('jbz', 'sqh'), ('nvg', 'vfj'))
    with open('day25.txt') as f:
        raw_connections = f.read()

connections = raw_connections.strip().splitlines()
nodes = {}
for line in connections:
    node, neighbours = line.split(': ')
    neighbours = neighbours.split(' ')
    if node not in nodes:
        nodes[node] = {neighbours[0]}
    else:
        nodes[node].add(neighbours[0])
    for _n in neighbours[1:]:
        nodes[node].add(_n)

    for _n in neighbours:
        if _n not in nodes:
            nodes[_n] = {node}
        else:
            nodes[_n].add(node)


def cut_edges(edges):
    # remove the given edges from the graph
    for (c1, c2) in edges:
        nodes[c1].remove(c2)
        nodes[c2].remove(c1)
        print(("Removed", f"{(c1, c2) = }"))


# cut the nodes
if has_cut:
    cut_edges(key_edges)

m_len = 0
for n in nodes:
    # print(n, nodes[n])
    m_len = max(m_len, len(nodes[n]))

from heapq import heappop, heappush

def find_random_path(start_vertex, end_vertex, path=None):
    """ find a path from start_vertex to end_vertex
        in graph """
    if path == None: # TO DO conditional seems redundant
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

def find_ni_random_path(start_vertex, end_vertex):
    """ iteratively find a path from start_vertex to end_vertex
        in graph """
    graph = nodes
    stack = [(start_vertex, [start_vertex])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex == end_vertex:
            return path
        neighbours = list(graph[vertex])
        random.shuffle(neighbours)
        for neighbour in neighbours:
            if neighbour not in path:
                stack.append((neighbour, path + [neighbour]))
                break
    return None



def find_path(start_vertex, end_vertex, path=None):
    """ find a path from start_vertex to end_vertex
        in graph """
    if path == None: # TO DO conditional seems redundant
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
k1,k2 = list(nodes.keys()), list(nodes.keys())
sz = len(k1)

def return_edges(path):
    e = set()
    for i in range(len(path) - 1):
        e.add(tuple(sorted([path[i], path[i + 1]])))
    return e

if not has_cut:
    # find nodes to cut
    for i in range(50):
        random.shuffle(k1)
        random.shuffle(k2)
        for node_0 in zip(k1[:sz], k2[:sz]):
            # print(node_0)
            rounds += 1
            pt = find_ni_random_path(node_0[0], node_0[1])
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

    print('SHould be: ', sorted(key_edges))
    print('         : ', sorted(s1), set(key_edges) == set(sorted(s1)))
else:
    set1 = set()
    founder1 = key_edges[0][0]
    set2 = set()
    founder2 = key_edges[0][1]
    t1 = time()
    while len(set1) + len(set2) - len(nodes.keys()):
        for founder_n, set_n, set_other in zip([founder1, founder2], [set1, set2], [set2, set1]):
            for i in list(nodes.keys()):
                for _ in range(1):
                    if i in set_other or i in set_n:
                        break
                    pt = find_ni_random_path(i, founder_n)
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
