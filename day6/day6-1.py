#!/usr/bin/env python3
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

graph = {}

with open('day6.txt') as input_file:
    for line in input_file:
        (key, val) = line.rstrip('\n').split(')')
        if key in graph.keys():
            graph[key].append(val)
        else:
            graph[key] = []
            graph[key].append(val)

total_orbits = {}

for key in graph:
    for n in graph[key]:
        (k, v) = n, len(find_path(graph, 'COM', n)) - 1
        if k in total_orbits.keys():
            continue
        else:
            total_orbits[k] = v

sum_orbits = sum(total_orbits.values())
print(sum_orbits)
