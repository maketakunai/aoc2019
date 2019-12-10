#!/usr/bin/env python3
from __future__ import division
import math, sys

class Coord(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def angle(a, b):
    return math.atan2(b.y - a.y, b.x - a.x)

def distance(a, b):
    return math.sqrt( (a.x - b.x)**2 + (a.y - b.y)**2 )

def find_shortest_distance(points, center):
    distances = []
    for n in range(len(points)):
        dist = distance(Coord(*points[n]), Coord(*center))
        distances.append([n, dist])
    distances = sorted(distances, key = lambda x: x[1])
    return points.pop(distances[0][0])

grid = []
asteroid_coords = []
sight_map = {}

with open('day10.txt') as input_file:
    for line in input_file:
        grid.append(list(line.rstrip('\n')))

for n in range(len(grid)):
    for m in range(len(grid[n])):
        if (grid[n][m] == '#'):
            asteroid_coords.append((m,n))

for asteroid_a in asteroid_coords:
    angles = set()
    for asteroid_b in asteroid_coords:
        if (asteroid_b == asteroid_a):
            continue
        else:
            angles.add(angle(Coord(*asteroid_b), Coord(*asteroid_a)))
    sight_map[asteroid_a] = len(angles)

max_num = max(sight_map, key=sight_map.get)

laser_angles = {}
for asteroid in asteroid_coords:
    if (asteroid == max_num):
        continue
    else:
        angl = (630.0 - math.degrees(angle(Coord(*max_num), Coord(*asteroid)))) % 360
        if angl not in laser_angles.keys():
            laser_angles[angl] = []
            laser_angles[angl].append(asteroid)
        else:
            laser_angles[angl].append(asteroid)


sorted_angles = sorted(laser_angles.keys())
sorted_angles = sorted_angles[::-1]
temp = sorted_angles.pop()
sorted_angles.insert(0, temp)

zapped = []
n = 0
found = 0
while (found is not 200):
    if (len( laser_angles[sorted_angles[n]] ) == 0):
        continue
    else:
        shortest = find_shortest_distance(laser_angles[sorted_angles[n]], max_num)
        zapped.append(shortest)
        n = ( n + 1 ) % len(sorted_angles)
        found += 1

print(zapped[-1])
print(zapped[-1][0]*100 + zapped[-1][1])
