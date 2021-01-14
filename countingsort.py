import math
import os
import random
import re
import sys
from operator import itemgetter

# Complete the countSort function below.
def countSort(arr):
    arr_size = len(arr)
    for i in range(arr_size):
        if i < arr_size / 2:
            arr[i][1] = '-'
        
        arr[i][0] = int(arr[i][0])
    
    arr_sorted = sorted(arr, key=itemgetter(0))
    string = ''
    for item in arr_sorted:
        string += item[1] + ' '
        
    print(string)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
