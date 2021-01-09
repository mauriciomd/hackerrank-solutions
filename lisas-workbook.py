#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.


def workbook(n, k, arr):
    current_page = 0
    total = 0

    for i in range(n):
        for problem in range(1, arr[i] + 1):
            if k > 1 and problem % k == 1:
                current_page += 1
            elif k == 1:
                current_page += 1

            if problem == current_page:
                total += 1

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
