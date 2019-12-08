#!/usr/bin/env python3

image_data = ''
width = 25
height = 6

def count_num_layer(layer, num):
    counter = 0
    for i in layer:
        counter += str(i).count(str(num))
    return counter

with open('day8.txt') as input_file:
    image_data = input_file.readline().rstrip('\n')

image_layers = [image_data[i:i+width] for i in range(0, len(image_data), width)]

separated_layers = {}

num_layers = len(image_data) / (width * height)

for n in range(0, num_layers):
    temp = []
    for _ in range(0, height):
        temp.append(image_layers.pop(0))
    separated_layers[n] = temp

zero_counter = {}

for layer in separated_layers:
    zero_counter[layer] = count_num_layer(separated_layers[layer], 0)

print(zero_counter)

min_zero_key = min(zero_counter, key=zero_counter.get)

print (count_num_layer(separated_layers[min_zero_key], 1) * count_num_layer(separated_layers[min_zero_key], 2))
