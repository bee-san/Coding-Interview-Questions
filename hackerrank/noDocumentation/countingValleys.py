#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # so instantly i'm thinking switch the DD UU to 1 and -1
    # so [DDUUUU] would become [-1, -1, 1, 1, 1, 1]
    # So a valley is determined when he goes below sea level
    # this solves that, because we always keep track of his elevation this way. if elevation < 0, hes in a valley
    # we then add + 1 to a counter until he goes above sea level again
    # Sooo, we go one by one through this list.
    # each new iter-item we check to see if evelation < 0
    # if it is, we add +1 to a counter. 
    # We also set inValley = True
    # if elevation < 0 and not inValley, we execute valley
    # else we don't, meaning we're still in the valley

    currentElevation = 0
    inValley = False
    valleys = 0
    for step in s:
        if step == "U":
            currentElevation += 1
        else:
            currentElevation -= 1
        if currentElevation < 0 and not inValley:
            inValley = True
            valleys += 1
        if currentElevation >= 0 and inValley:
            inValley = False
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
