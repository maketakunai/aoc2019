#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import intcode_computer as i_c

def instructions(input, panel, robot, painted):

    def color_square(p):
        if (input[0] == 0):
            panel[p[0]][p[1]] = '.'
        else:
            panel[p[0]][p[1]] = '#'
        painted.add( (p[0],p[1]) )

    def from_up_move():
        if (input[1]):
            prev = robot_data[0][:]
            robot_data[0][1] += 1
            next = panel[robot_data[0][0]][robot_data[0][1]]
            robot_data[1] = '>'
            color_square(prev)
            panel[robot_data[0][0]][robot_data[0][1]] = robot_data[1]
            return next
        else:
            prev = robot_data[0][:]
            robot_data[0][1] -= 1
            next = panel[robot_data[0][0]][robot_data[0][1]]
            robot_data[1] = '<'
            color_square(prev)
            panel[robot_data[0][0]][robot_data[0][1]] = robot_data[1]
            return next

    def from_left_move():
        if (input[1]):
            prev = robot_data[0][:]
            robot_data[0][0] -= 1
            next = panel[robot_data[0][0]][robot_data[0][1]]
            robot_data[1] = '^'
            color_square(prev)
            panel[robot_data[0][0]][robot_data[0][1]] = robot_data[1]
            return next
        else:
            prev = robot_data[0][:]
            robot_data[0][0] += 1
            next = panel[robot_data[0][0]][robot_data[0][1]]
            robot_data[1] = 'v'
            color_square(prev)
            panel[robot_data[0][0]][robot_data[0][1]] = robot_data[1]
            return next

    def from_right_move():
        if (input[1]):
            prev = robot_data[0][:]
            robot_data[0][0] += 1
            next = panel[robot_data[0][0]][robot_data[0][1]]
            robot_data[1] = 'v'
            color_square(prev)
            panel[robot_data[0][0]][robot_data[0][1]] = robot_data[1]
            return next
        else:
            prev = robot_data[0][:]
            robot_data[0][0] -= 1
            next = panel[robot_data[0][0]][robot_data[0][1]]
            robot_data[1] = '^'
            color_square(prev)
            panel[robot_data[0][0]][robot_data[0][1]] = robot_data[1]
            return next

    def from_down_move():
        if (input[1]):
            prev = robot_data[0][:]
            robot_data[0][1] -= 1
            next = panel[robot_data[0][0]][robot_data[0][1]]
            robot_data[1] = '<'
            color_square(prev)
            panel[robot_data[0][0]][robot_data[0][1]] = robot_data[1]
            return next
        else:
            prev = robot_data[0][:]
            robot_data[0][1] += 1
            next = panel[robot_data[0][0]][robot_data[0][1]]
            robot_data[1] = '>'
            color_square(prev)
            panel[robot_data[0][0]][robot_data[0][1]] = robot_data[1]
            return next

    if (robot[1] == '^'):
        return from_up_move()
    elif (robot[1] == '<'):
        return from_left_move()
    elif (robot[1] == '>'):
        return from_right_move()
    elif (robot[1] == 'v'):
        return from_down_move()


width = 100
height = 100
panel = [['.' for x in range(width)] for y in range(height)]
start_point = [50, 50]
panel[start_point[0]][start_point[1]] = '^'
robot_data = [start_point, '^']
painted = set()

intcode = []
with open('day11.txt') as input_file:
    intcode = [int(d) for d in input_file.readline().split(',')]

intcode.extend([0] * 100000)
terminate = False
input = 1
#input = 0
state_pointer = 0
base = 0

while not terminate:
    state_pointer, terminate, instr, intcode, base = i_c.calculation(intcode, state_pointer, input, base)
    if (terminate):
        break
    a = instructions(instr, panel, robot_data, painted)
    input = 0 if (a == '.') else 1


for line in panel:
    print(''.join(map(str, line)).replace('#', '█').replace('.','░'))
print(len(painted))
