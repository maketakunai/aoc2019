#!/usr/bin/env python3

def priority(ins, n, parameter):
    if (parameter == 0):
        return ins[ins[n]]
    elif (parameter == 1):
        return ins[n]

def get_params(ins):
    if (len(str(ins)) > 2):
        opcode = ins % 100
        parameters = [int(d) for d in str(ins // 100)][::-1]
        if (len(parameters) == 1):
            parameters.append(0)
        return opcode, parameters
    else:
        opcode = ins
        parameters = [0,0]
        return opcode, parameters

def calculation(instructions):
    n = 0
    while (n < len(instructions)):
        opcode, parameters = get_params(instructions[n])
        if (opcode == 1):
            instructions[instructions[n+3]] = priority(instructions, n+1, parameters[0]) + priority(instructions, n+2, parameters[1])
            n += 4
        elif (opcode == 2):
            instructions[instructions[n+3]] = priority(instructions, n+1, parameters[0]) * priority(instructions, n+2, parameters[1])
            n += 4
        elif (opcode == 3):
            user_input = input()
            instructions[instructions[n+1]] = int(user_input)
            n += 2
        elif (opcode == 4):
            print(priority(instructions, n+1, parameters[0]))
            n += 2
        elif (opcode == 5):
            if (priority(instructions, n+1, parameters[0]) != 0):
                n = priority(instructions, n+2, parameters[1])
            else:
                n += 3
        elif (opcode == 6):
            if (priority(instructions, n+1, parameters[0]) == 0):
                n = priority(instructions, n+2, parameters[1])
            else:
                n += 3
        elif (opcode == 7):
            if (priority(instructions, n+1, parameters[0]) < priority(instructions, n+2, parameters[1])):
                instructions[instructions[n+3]] = 1
                n += 4
            else:
                instructions[instructions[n+3]] = 0
                n += 4
        elif (opcode == 8):
            if (priority(instructions, n+1, parameters[0]) == priority(instructions, n+2, parameters[1])):
                instructions[instructions[n+3]] = 1
                n += 4
            else:
                instructions[instructions[n+3]] = 0
                n += 4
        elif (opcode == 99):
            break
        else:
            print ("Invalid instruction:", opcode)
            n += 1


intcode = []
with open('day5.txt') as input_file:
    intcode = [int(d) for d in input_file.readline().split(',')]

calculation(intcode)
