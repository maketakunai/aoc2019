#!/usr/bin/env python3

def priority(ins, n, parameter, r_base):
    if (parameter == 0):
        return ins[ins[n]]
    elif (parameter == 1):
        return ins[n]
    elif (parameter == 2):
        new_pos = r_base + ins[n]
        return ins[new_pos]

def get_params(ins):
    if (len(str(ins)) > 2):
        opcode = ins % 100
        parameters = [int(d) for d in str(ins // 100)][::-1]
        if (len(parameters) == 1):
            parameters.extend([0] * 2)
        elif (len(parameters) == 2):
            parameters.extend([0] * 1)
        return opcode, parameters
    else:
        opcode = ins
        parameters = [0,0,0]
        return opcode, parameters

def save_idx(ins, n, parameter, r_base):
    if (parameter == 2):
        return (ins[n] + r_base)
    else:
        return ins[n]

def calculation(instructions):
    n = 0
    r_base = 0
    while (n < len(instructions)):
        opcode, parameters = get_params(instructions[n])
        if (opcode == 1):
            instructions[save_idx(instructions, n+3, parameters[2], r_base)] = priority(instructions, n+1, parameters[0], r_base) + priority(instructions, n+2, parameters[1], r_base)
            n += 4
        elif (opcode == 2):
            instructions[save_idx(instructions, n+3, parameters[2], r_base)] = priority(instructions, n+1, parameters[0], r_base) * priority(instructions, n+2, parameters[1], r_base)
            n += 4
        elif (opcode == 3):
            user_input = input()
            instructions[save_idx(instructions, n+1, parameters[0], r_base)] = int(user_input)
            n += 2
        elif (opcode == 4):
            print(priority(instructions, n+1, parameters[0], r_base))
            n += 2
        elif (opcode == 5):
            if (priority(instructions, n+1, parameters[0], r_base) != 0):
                n = priority(instructions, n+2, parameters[1], r_base)
            else:
                n += 3
        elif (opcode == 6):
            if (priority(instructions, n+1, parameters[0], r_base) == 0):
                n = priority(instructions, n+2, parameters[1], r_base)
            else:
                n += 3
        elif (opcode == 7):
            if (priority(instructions, n+1, parameters[0], r_base) < priority(instructions, n+2, parameters[1], r_base)):
                instructions[save_idx(instructions, n+3, parameters[2], r_base)] = 1
                n += 4
            else:
                instructions[save_idx(instructions, n+3, parameters[2], r_base)] = 0
                n += 4
        elif (opcode == 8):
            if (priority(instructions, n+1, parameters[0], r_base) == priority(instructions, n+2, parameters[1], r_base)):
                instructions[save_idx(instructions, n+3, parameters[2], r_base)] = 1
                n += 4
            else:
                instructions[save_idx(instructions, n+3, parameters[2], r_base)] = 0
                n += 4
        elif (opcode == 9):
            r_base += priority(instructions, n+1, parameters[0], r_base)
            n += 2
        elif (opcode == 99):
            break
        else:
            print ("Invalid instruction:", opcode)
            break


intcode = []
with open('day9.txt') as input_file:
    intcode = [int(d) for d in input_file.readline().split(',')]

intcode.extend([0] * 100000)
calculation(intcode)
