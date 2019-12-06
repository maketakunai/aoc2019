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

san_path = find_path(graph, 'COM', 'SAN')
you_path = find_path(graph, 'COM', 'YOU')

prev_match = san_path[0]
for (x,y) in zip(san_path, you_path):
    if (x == y):
        prev_match = x
        continue
    else:
        break

path_between = len(find_path(graph, prev_match, 'SAN')) + len(find_path(graph, prev_match, 'YOU')) - 4
print(path_between)
