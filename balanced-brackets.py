#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    
    for entry in s:
        if entry == '(' or entry == '[' or entry == '{':
            stack.append(entry)
        else:
            if len(stack) == 0:
                return 'NO'
            
            data = stack.pop()
            if data == '(' and entry != ')':
                return 'NO'
            elif data == '[' and entry != ']':
                return 'NO'
            elif data == '{' and entry != '}':
                return 'NO'
    
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
