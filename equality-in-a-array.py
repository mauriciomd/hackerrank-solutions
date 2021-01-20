#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.


def equalizeArray(arr):
    occurrences = {}
    max_occurrences = 1

    for element in arr:
        if element not in occurrences:
            occurrences[element] = 1
        else:
            occurrences[element] += 1
            if occurrences[element] > max_occurrences:
                max_occurrences = occurrences[element]

    return len(arr) - max_occurrences


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
