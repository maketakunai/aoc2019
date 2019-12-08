#!/usr/bin/env python3
# -*- coding: utf-8 -*-

image_data = ''
width = 25
height = 6

def count_num_layer(layer, num):
    counter = 0
    for i in layer:
        counter += str(i).count(str(num))
    return counter

def layer_comp(layer, final):
    for x in range(len(layer)):
        for y in range(len(layer[x])):
            if (final[x][y] == 0 or final[x][y] == 1):
                continue
            elif(int(layer[x][y]) < final[x][y]):
                final[x][y] = int(layer[x][y])

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

final_image = [ [3]*width for i in range(height)]


for layer in separated_layers:
    layer_comp(separated_layers[layer], final_image)

for line in final_image:
    print(''.join(map(str, line)).replace('0', '█').replace('1','░'))
