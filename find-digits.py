#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.


def findDigits(n):
    digits = list(map(int, str(n)))
    total = 0

    for d in digits:
        if d > 0:
            if n % d == 0:
                total += 1

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
