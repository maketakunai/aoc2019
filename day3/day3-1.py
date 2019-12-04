#!/usr/bin/env python3
wires = []

with open('day3.txt') as input_file:
    for line in input_file:
        wires.append(line.rstrip('\n').split(','))

#translate into coord system
def gen_coords(wire):
    wire_coords = []
    x, y = 0, 0
    for n in wire:
        if (n[0] == 'U'):
            y += int(filter(str.isdigit, n))
            wire_coords.append([x,y])
        if (n[0] == 'D'):
            y -= int(filter(str.isdigit, n))
            wire_coords.append([x,y])
        if (n[0] == 'R'):
            x += int(filter(str.isdigit, n))
            wire_coords.append([x,y])
        if (n[0] == 'L'):
            x -= int(filter(str.isdigit, n))
            wire_coords.append([x,y])
    return wire_coords

def check_intersection(w1p, w1q, w2p, w2q):
    if (w1p[0] - w1q[0] == 0 and w2p[0] - w2q[0] == 0):
        return False
    elif (w1p[1] - w1q[1] == 0 and w2p[1] - w2q[1] == 0):
        return False

    if (w1p[0] - w1q[0] == 0):
        if (w1p[0] >= min(w2p[0], w2q[0]) and w1p[0] <= max(w2p[0], w2q[0]) and w2p[1] >= min (w1p[1], w1q[1]) and w2p[1] <= max (w1p[1], w1q[1])):
            return [w1p[0], w2p[1]]
        else:
            return False
    else:
        if (w1p[1] >= min(w2p[1], w2q[1]) and w1p[1] <= max(w2p[1], w2q[1]) and w2p[0] >= min (w1p[0], w1q[0]) and w2p[0] <= max (w1p[0], w1q[0])):
            return [w1p[1], w2p[0]]
        else:
            return False

wire1, wire2 = [], []

wire1 = gen_coords(wires[0])
wire2 = gen_coords(wires[1])

distances = []

for a in range(0, len(wire1) - 1):
    for b in range(0, len(wire2) - 1):
        coords = check_intersection(wire1[a], wire1[a+1], wire2[b], wire2[b+1])
        if ( coords ):
            distances.append( abs(coords[0])+abs(coords[1]) )
print(distances)
print(min(distances))
