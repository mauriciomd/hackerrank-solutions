#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.


def whatFlavors(cost, money):
    diff_cost_table = {}
    cost_arr_len = len(cost)

    for i in range(1, cost_arr_len + 1):
        diff = money - cost[i-1]
        if diff not in diff_cost_table:
            diff_cost_table[diff] = i

        if cost[i-1] in diff_cost_table and diff_cost_table[cost[i-1]] != i:
            print(f'{diff_cost_table[cost[i-1]]} {i}')


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
