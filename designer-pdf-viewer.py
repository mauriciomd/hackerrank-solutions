#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    max_h = 0
    
    for ch in word:
        letter_index = ord(ch) - ord('a')
        if h[letter_index] > max_h:
            max_h = h[letter_index]
    
    return len(word) * max_h

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
