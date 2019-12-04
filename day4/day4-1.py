#!/usr/bin/env python3

def is_increasing(num):
    return (num[5] >= num[4] and num[4] >= num[3] and num[3] >= num[2] and num[2] >= num[1] and num[1] >= num[0])

def uniques(num):
    my_set = set(char for char in num)
    if (len(my_set) > 5):
        return False
    else:
        return True

input_start = 245318
input_end = 765747
counter = 0

for n in range(input_start, input_end):
    if ( is_increasing(str(n)) and uniques(str(n)) ):
        counter += 1

print(counter)
