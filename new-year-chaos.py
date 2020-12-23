#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    total = 0
    
    for i, value in enumerate(q):
        index = i + 1
        diff = value - index
        if diff >= 3:
            print('Too chaotic')
            return
        
        print('\n')
        for j in range(max(value - 2, 0), index):
            print(j, q[j], value)
            if q[j] > value:
                total += 1
        print('\n')
        
                
    print(total)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
