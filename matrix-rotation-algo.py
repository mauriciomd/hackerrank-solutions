#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    rows = len(matrix)
    cols = len(matrix[0])
    layers = int(min(rows, cols) / 2)
    
    matrix_placeholder = []
    current_layer = 0
    
    for current_layer in range(layers):
        matrix_placeholder.append([])
        for i in range(cols - current_layer - 1, current_layer, -1):
            matrix_placeholder[current_layer].append(matrix[current_layer][i])
        
        for i in range(current_layer, rows - current_layer):
            matrix_placeholder[current_layer].append(matrix[i][current_layer])
        
        for i in range(current_layer + 1, cols - current_layer):
            matrix_placeholder[current_layer].append(matrix[rows - current_layer - 1][i])
        
        for i in range(rows - current_layer - 2, current_layer, - 1):
            matrix_placeholder[current_layer].append(matrix[i][cols - current_layer - 1])
    
    
    for current_layer in range(layers):
        layer_size = len(matrix_placeholder[current_layer])
        real_rotation = r % layer_size
        layer_index = layer_size - real_rotation if real_rotation > 0 else 0

        for i in range(cols - current_layer - 1, current_layer, -1):
            matrix[current_layer][i] = matrix_placeholder[current_layer][layer_index]
            layer_index += 1
            
            if layer_index >= layer_size:
                layer_index -= layer_size
        
        for i in range(current_layer, rows - current_layer):
            matrix[i][current_layer] = matrix_placeholder[current_layer][layer_index]
            layer_index += 1
            
            if layer_index >= layer_size:
                layer_index -= layer_size
        
        for i in range(current_layer + 1, cols - current_layer):
            matrix[rows - current_layer - 1][i] = matrix_placeholder[current_layer][layer_index]
            layer_index += 1
            
            if layer_index >= layer_size:
                layer_index -= layer_size
    
        for i in range(rows - current_layer - 2, current_layer, - 1):
            matrix[i][cols - current_layer - 1] = matrix_placeholder[current_layer][layer_index]
            layer_index += 1
            
            if layer_index >= layer_size:
                layer_index -= layer_size
    
    
    for line in matrix:
        print(" ".join(map(str, line)))

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
