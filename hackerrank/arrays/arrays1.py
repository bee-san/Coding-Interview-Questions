#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # as theres 4 glasses
    sumList = []
    i = 0
    print(arr)
    for x in range(0, len(arr) - 2):
        for j in range(0, len(arr) - 2):
            sumList.append(arr[x][j] + arr[x][j+1] + arr[x][j+2] + arr[x+1][j+1] + arr[x+2][j] + arr[x+2][j+1] + arr[x+2][j+2])

    return max(sumList)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
