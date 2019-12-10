#!/usr/bin/env python3
from __future__ import division
import math

class Coord(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def angle(a, b):
    return math.atan2(b.y - a.y, b.x - a.x)

grid = []

with open('day10.txt') as input_file:
    for line in input_file:
        grid.append(list(line.rstrip('\n')))

asteroid_coords = []

for n in range(len(grid)):
    for m in range(len(grid[n])):
        if (grid[n][m] == '#'):
            asteroid_coords.append((n,m))

sight_map = {}

for asteroid_a in asteroid_coords:
    angles = set()
    for asteroid_b in asteroid_coords:
        if (asteroid_b == asteroid_a):
            continue
        else:
            angles.add(angle(Coord(*asteroid_b), Coord(*asteroid_a)))
    sight_map[asteroid_a] = len(angles)

#print (sight_map)
max_num = max(sight_map, key=sight_map.get)
print (sight_map[max_num])
