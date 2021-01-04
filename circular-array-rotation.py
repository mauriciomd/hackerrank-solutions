#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.


def circularArrayRotation(a, k, queries):
    arr_size = len(a)
    n_rotation = k % arr_size
    start_index = arr_size - n_rotation

    new_arr = []
    for current_index in range(arr_size):
        x = start_index + current_index
        if x >= arr_size:
            x -= arr_size
        new_arr.append(a[x])

    return [new_arr[i] for i in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
