#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.


def viralAdvertising(n):
    initial_people = 5
    people = initial_people
    likes = 0

    for _ in range(n):
        likes += math.floor(people / 2)
        people = math.floor(people / 2) * 3

    return likes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
