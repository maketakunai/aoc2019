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

def get_steps (input, wires):
    steps_a, steps_b = 0, 0
    all_steps = []
    for set in input:
        for n in range(0, set[0]):
            steps_a += int(filter(str.isdigit, wires[0][n]))
        for m in range(0, set[1]):
            steps_b += int(filter(str.isdigit, wires[1][m]))
        all_steps.append(steps_a+steps_b+set[2])
    return all_steps


def intersect_steps (coords, w1, w2, w1_input, w2_input, steps_a, steps_b):
    additional_steps = 0
    if (w1_input[steps_a][0] == 'D'):
        additional_steps += abs(w1[1]-coords[1])
    if (w1_input[steps_a][0] == 'U'):
        additional_steps += abs(coords[1]-w1[1])
    if (w1_input[steps_a][0] == 'R'):
        additional_steps += abs(coords[0]-w1[0])
    if (w1_input[steps_a][0] == 'L'):
        additional_steps += abs(w1[0]-coords[0])
    if (w2_input[steps_b][0] == 'D'):
        additional_steps += abs(w2[1]-coords[1])
    if (w2_input[steps_b][0] == 'U'):
        additional_steps += abs(coords[1]-w2[1])
    if (w2_input[steps_b][0] == 'R'):
        additional_steps += abs(coords[0]-w2[0])
    if (w2_input[steps_b][0] == 'L'):
        additional_steps += abs(w2[0]-coords[0])
    return additional_steps

wire1, wire2 = [], []


wire1 = gen_coords(wires[0])
wire2 = gen_coords(wires[1])

distances = []
steps_a = 0
stepcounts = []

for a in range(0, len(wire1) - 1):
    steps_a += 1
    steps_b = 0
    for b in range(0, len(wire2) - 1):
        steps_b +=1
        coords = check_intersection(wire1[a], wire1[a+1], wire2[b], wire2[b+1])
        if ( coords ):
            distances.append( abs(coords[0])+abs(coords[1]) )
            steps_to_intersect = intersect_steps(coords, wire1[a], wire2[b], wires[0], wires[1], steps_a, steps_b)
            stepcounts.append([steps_a,steps_b, steps_to_intersect])

all_steps = get_steps(stepcounts, wires)
print(min(all_steps))
