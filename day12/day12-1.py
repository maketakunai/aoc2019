#!/usr/bin/env python3

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


zeroes = [ 0 for x in range(3) ]

p1 = Planet(14, 2, 8, *zeroes)
p2 = Planet(7, 4, 10, *zeroes )
p3 = Planet(1, 17, 16, *zeroes)
p4 = Planet(-4, -1, 1, *zeroes)

planets = [p1, p2, p3, p4]
steps = 0

while (steps < 1000):
    calc_gravity(planets)
    apply_velocity(planets)
    steps += 1

e = total_energy(planets)
print(e)
