#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    lenght = len(c)
    jumps = 0

    i = 0
    while i < lenght - 1:
        if c[i+1] == 1:
            i += 2
            jumps += 1
            continue

        if i + 2 < lenght:
            if c[i+1] == 0 and c[i+2] == 0:
                i += 2
                jumps += 1
                continue

        i += 1
        jumps += 1

    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
