#!/usr/bin/env python3

import fileinput

total_fuel = 0

def calc_fuel(n):
    return (int(n) // 3) - 2

for line in fileinput.input():
    fuel = calc_fuel(line)
    temp_count = fuel
    while (fuel >= 0):
        fuel = calc_fuel(fuel)
        if (fuel >= 0):
            temp_count += fuel
    total_fuel += temp_count

print(total_fuel)
