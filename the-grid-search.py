#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.


def gridSearch(G, P):
    grid_rows = len(G)
    grid_cols = len(G[0])
    pattern_rows = len(P)
    pattern_cols = len(P[0])
    matches = 0

    for i in range(grid_rows - pattern_rows + 1):
        for j in range(grid_cols - pattern_cols + 1):
            if G[i][j:j+pattern_cols] == P[0]:
                for k in range(pattern_rows):
                    if G[i+k][j:j+pattern_cols] == P[k]:
                        matches += 1
                        if matches == pattern_rows:
                            return 'YES'
                    else:
                        matches = 0

    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
