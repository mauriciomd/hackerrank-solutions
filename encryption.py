#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    string = s.replace(' ', '')
    
    str_len = len(string)
    square_root = str_len ** 0.5
    num_of_rows = int(math.floor(square_root))
    num_of_cols = int(math.ceil(square_root))

    if num_of_rows * num_of_cols < str_len:
        num_of_rows += 1

    matrix = []
    str_index = 0
    for i in range(num_of_rows):
        matrix.append([])
        for _ in range(num_of_cols):
            if str_index < str_len:
                matrix[i].append(string[str_index])
                str_index += 1
            else:
                matrix[i].append('')
    
    encrypted_string = ''
    for i in range(num_of_cols):
        for j in range(num_of_rows):
            if matrix[j][i] != '':
                encrypted_string += matrix[j][i]
        
        if i < num_of_cols - 1:
            encrypted_string += ' '
            
    return encrypted_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
