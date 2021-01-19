#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    occurrences = 0
    str_len = len(s)

    for char in s:
        if char == 'a':
            occurrences += 1

    if n == 1:
        return occurrences

    module = n % str_len
    occurrences *= n // str_len

    if module > 0:
        for i in range(module):
            if s[i] == 'a':
                occurrences += 1

    return occurrences


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
