#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bfs function below.


def bfs(n, m, edges, s):
    graph = {}
    for index in range(1, n+1):
        graph[index] = set()

    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    queue = [(graph[s], 0)]
    visited = []
    weights = {}

    while len(queue) > 0:
        item = queue.pop(0)

        for node in item[0]:
            if node not in visited and node != s:
                visited.append(node)
                queue.append((graph[node], item[1] + 6))
                weights[node] = item[1] + 6

    result = []
    for node in range(1, n+1):
        if node != s:
            result.append(weights.get(node, -1))

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
