#!/bin/python3

import math
import os
import random
import re
import sys

# Reference used to solve this challenge: 
#   -- https://en.wikipedia.org/wiki/Parity_of_a_permutation
# Complete the larrysArray function below.
def larrysArray(A):
    num_of_swaps = 0
    arr_len = len(A)
    
    j = 1
    while j < arr_len:
        i = j -1
        value = A[j]
        while i >= 0 and A[i] > value:
            A[i+1] = A[i]
            num_of_swaps += 1
            i -= 1
        A[i+1] = value
        j += 1
        
    if num_of_swaps % 2 == 0:
        return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
