#!/usr/bin/env python3
import itertools

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

def calculation(instructions, phase, input, state, input_flag):
    n = state
    prog_output = 0
    internal_flag = 0
    while (n < len(instructions)):
        opcode, parameters = get_params(instructions[n])
        if (opcode == 1):
            instructions[instructions[n+3]] = priority(instructions, n+1, parameters[0]) + priority(instructions, n+2, parameters[1])
            n += 4
        elif (opcode == 2):
            instructions[instructions[n+3]] = priority(instructions, n+1, parameters[0]) * priority(instructions, n+2, parameters[1])
            n += 4
        elif (opcode == 3):
            if (not input_flag and internal_flag == 0):
                instructions[instructions[n+1]] = phase
                n += 2
                internal_flag = 1
            else:
                instructions[instructions[n+1]] = input
                n += 2
        elif (opcode == 4):
            prog_output = priority(instructions, n+1, parameters[0])
            n += 2
            return (prog_output, n, False)
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
    return (prog_output, n, True)


intcode = []
with open('day7.txt') as input_file:
    intcode = [int(d) for d in input_file.readline().split(',')]

phase_settings = list(itertools.permutations([5,6,7,8,9], 5))

final_answer = []
for phase_combination in phase_settings:
    intcode_lists = [intcode[:] for i in range(5)]
    machine_states = [0 for j in range(5)]
    terminate = False
    input_flag = False
    phase_output = [0]
    phase = 0
    while not terminate:
        calc_result = calculation(intcode_lists[phase], phase_combination[phase], phase_output[-1], machine_states[phase], input_flag)
        phase_output.append(calc_result[0])
        machine_states[phase] = calc_result[1]
        terminate = calc_result[2]
        phase = (phase + 1) % 5
        if phase == 0:
            input_flag = True
    final_answer.append(phase_output[-2])

print(max(final_answer))
