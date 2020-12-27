#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the counterGame function below.
def counterGame(n):
    winner = 'Richard'
    
    while n > 1:
        n_binary = bin(n).replace('0b', '')
        lower_power_of_two = '1'
        for _ in range(1, len(n_binary)):
            lower_power_of_two += '0'
            
        diff = int(n_binary, 2) - int(lower_power_of_two, 2)
        if diff == 0:
            n = int(n / 2)
        else:
            n = diff
            
        if winner == 'Richard':
            winner = 'Louise'
        else:
            winner = 'Richard'
    
    return winner
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
