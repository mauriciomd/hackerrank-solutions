#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.


def utopianTree(n):
    tree_height = 1

    if n == 0:
        return tree_height

    for num in range(1, n + 1):
        if num % 2 == 1:
            tree_height *= 2
        else:
            tree_height += 1

    return tree_height


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
