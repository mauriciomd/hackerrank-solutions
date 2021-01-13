#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.


def cutTheSticks(arr):
    answer = [len(arr)]

    while True:
        min_value = min(arr)
        arr = [x - min_value for x in arr if x - min_value > 0]
        if len(arr) == 0:
            break
        else:
            answer.append(len(arr))

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
