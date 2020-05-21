#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # so obviously minimum would be an O(n) algorithm
    # she can jump 1 block or 2 blocks ahead. 
    # so we want to jump if the cloud 2 clouds ahead is safe (0)
    # or if the cloud in front of us is unsafe (1)
    print(c)
    length = len(c)
    totalJumps = 0
    i = 0
    # while we are below the length of the array - 1, keep jumping
    while i < length - 1:
        # if we can double jump, then add + 1 to i to indicate double jumping
        if i + 2 < len(c) and c[i + 2] != 1:
            i += 1
        # single jump. if we can double jump, we effectively, in code, single jump twice
        i += 1
        totalJumps += 1
    return totalJumps

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
