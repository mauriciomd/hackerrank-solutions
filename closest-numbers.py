#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    pairs = []
    smallest_difference = float('inf')
    sorted_arr = sorted(arr)
    arr_size = len(sorted_arr)
    
    for i in range(arr_size - 1):
        value = value = sorted_arr[i+1] - sorted_arr[i]
        if value < smallest_difference:
            smallest_difference = value

            
    for i in range(arr_size - 1):
        value = value = sorted_arr[i+1] - sorted_arr[i]
        if value == smallest_difference:
            pairs.append(sorted_arr[i])
            pairs.append(sorted_arr[i+1])
        
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
