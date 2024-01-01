# day 25
# https://www.reddit.com/r/adventofcode/comments/18qbsxs/comment/kf12xgf/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# https://python-course.eu/applications-python/graphs-python.php
# https://www.reddit.com/r/adventofcode/comments/18qbsxs/comment/keuafrl/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# https://en.wikipedia.org/wiki/Bipartite_graph

# Finding which edges to cut to make this graph a bipartite graph fails sometimes while following the
# random path finding algorithm (find_ni_random_path). Does changing it to a non-random path finding
# algorithm change its behaviour? 30/12/23

import random
from time import time
import heapq
from typing import List, Tuple, Any

testing = False
to_search = True
to_cut = True

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


def cut_edges(edges):
    # remove the given edges from the graph
    print("Removing edges... ", end="")
    ch = ""
    for (c1, c2) in edges:
        nodes[c1].remove(c2)
        nodes[c2].remove(c1)
        print(f"{ch}{(c1, c2)}", end="")
        ch = ", "
    print()


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


def find_ni_path(start_vertex, end_vertex):
    """ iteratively find a path from start_vertex to end_vertex
        in graph """
    graph = nodes
    stack = [(start_vertex, [start_vertex])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex == end_vertex:
            return path
        neighbours = list(graph[vertex])
        for neighbour in neighbours:
            if neighbour not in path:
                stack.append((neighbour, path + [neighbour]))
                break
    return None


def bfs(f1, f2, s1, s2, graph):
    for (f, s, other) in zip([f1, f2], [s1, s2], [s2, s1]):
        idx = 0

        q: list[tuple[int, str]] = [(idx, f)]
        while q:
            idx += 1
            _, current = heapq.heappop(q)
            neighbours = graph[current]
            for n in neighbours:
                if n in other:
                    print("*" * 40, "\n", "This is NOT a bipartite graph", "\n", "*" * 40)
                    return 1
                if n not in s:
                    s.add(n)
                    heapq.heappush(q, (idx, n))
    return 0


def return_edges(path):
    e = set()
    for idx in range(len(path) - 1):
        e.add(tuple(sorted([path[idx], path[idx + 1]])))
    return e


# test this a certain number of times
for _ in range(1):

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

    k1, k2 = list(nodes.keys()), list(nodes.keys())

    edge_frequencies = {}

    if to_search:
        # find edges to cut
        # @ 20 random path repetitions no failures in 40 tests
        # @ 10 random path repetitions 4/40 failures
        # @  5 non-random path repetitions 16/16 failures
        # @  5 random path repetitions 18/40 failures
        # @  1 random path repetitions 40/40 failures

        t1 = time()
        _n = 20

        for i in range(_n):
            random.shuffle(k1)
            random.shuffle(k2)
            for node_0 in zip(k1, k2):
                pt = find_ni_path(node_0[0], node_0[1])
                if pt is not None:
                    for n in return_edges(pt):
                        if n in edge_frequencies:
                            edge_frequencies[n] += 1
                        else:
                            edge_frequencies[n] = 1
        print(f"Finished looking for edges to cut ({_n} rounds) in {time() - t1:.1f} s.")

        _s = []
        for (x, _) in sorted(list(edge_frequencies.items()), key=lambda z: z[1])[-3:]:
            _s.append(x)

        print('Observed: ', sorted(_s), set(key_edges) == set(_s))

        key_edges = _s

    # cut the nodes
    cut_edges(key_edges)

    set1, set2 = set(), set()
    founder1, founder2 = key_edges[0]

    t1 = time()
    bfs(founder1, founder2, set1, set2, nodes)
    print(f"Time needed to confirm whether this is a bipartite graph: {time() - t1:.5f} s")

    print(f"{len(nodes.keys()) = }, {len(set1) = },  {len(set2) = }")
    print(f"{len(set1) + len(set2) - len(nodes.keys()) = }")
    print(f"{len(set1) * len(set2) = }")
    print()
