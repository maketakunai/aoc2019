#!/usr/bin/env python3
import numpy as np

class Planet(object):
    def __init__(self, px, py, pz, vx, vy, vz):
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz

def velo_change(a, b):
    if (a.px == b.px):
        a.vx += 0
    elif (a.px < b.px):
        a.vx += 1
    elif (a.px > b.px):
        a.vx -= 1
    if (a.py == b.py):
        a.vy += 0
    elif (a.py < b.py):
        a.vy += 1
    elif (a.py > b.py):
        a.vy -= 1
    if (a.pz == b.pz):
        a.vz += 0
    elif (a.pz < b.pz):
        a.vz += 1
    elif (a.pz > b.pz):
        a.vz -= 1

def calc_gravity(p):
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i] == p[j]:
                continue
            else:
                velo_change(p[i], p[j])

def apply_velocity(p):
    for planet in p:
        planet.px += planet.vx
        planet.py += planet.vy
        planet.pz += planet.vz

def total_energy(p):
    energy = 0
    for planet in p:
        energy += (abs(planet.px)+abs(planet.py)+abs(planet.pz)) * (abs(planet.vx)+abs(planet.vy)+abs(planet.vz))
    return energy

def fetch_values(p1, p2, p3, p4, var):
    if (var == 'x'):
        return (p1.px, p2.px, p3.px, p4.px, p1.vx, p2.vx, p3.vx, p4.vx)
    if (var == 'y'):
        return (p1.py, p2.py, p3.py, p4.py, p1.vy, p2.vy, p3.vy, p4.vy)
    if (var == 'z'):
        return (p1.pz, p2.pz, p3.pz, p4.pz, p1.vz, p2.vz, p3.vz, p4.vz)

zeroes = [ 0 for x in range(3) ]

p1 = Planet(14, 2, 8, *zeroes)
p2 = Planet(7, 4, 10, *zeroes)
p3 = Planet(1, 17, 16, *zeroes)
p4 = Planet(-4, -1, 1, *zeroes)

#p1 = Planet(-8, -10, 0, *zeroes)
#p2 = Planet(5, 5, 10, *zeroes)
#p3 = Planet(2, -7, 3, *zeroes)
#p4 = Planet(9, -8, -3, *zeroes)

planets = [p1, p2, p3, p4]
steps = 0

seen_x = set()
seen_y = set()
seen_z = set()
repeat_x = None
repeat_y = None
repeat_z = None
flag_x = False
flag_y = False
flag_z = False

while (steps < 10000000000):
    if repeat_x and repeat_y and repeat_z:
        break
    temp_x = fetch_values(p1, p2, p3, p4, 'x')
    temp_y = fetch_values(p1, p2, p3, p4, 'y')
    temp_z = fetch_values(p1, p2, p3, p4, 'z')
    if temp_x in seen_x and not flag_x:
        repeat_x = steps
        flag_x = True
    else:
        seen_x.add(temp_x)
    if temp_y in seen_y and not flag_y:
        repeat_y = steps
        flag_y = True
    else:
        seen_y.add(temp_y)
    if temp_z in seen_z and not flag_z:
        repeat_z = steps
        flag_z = True
    else:
        seen_z.add(temp_z)
    calc_gravity(planets)
    apply_velocity(planets)
    steps += 1

print(repeat_x, repeat_y, repeat_z)

print(np.lcm.reduce([repeat_x, repeat_y, repeat_z]))
