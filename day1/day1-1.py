#!/usr/bin/env python3

import fileinput

total_fuel = 0

for line in fileinput.input():
    total_fuel += (int(line) // 3) - 2

print(total_fuel)
