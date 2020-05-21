#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # now we calculate how many time the letter a appears in the string
    countStart = s.count("a")
    # then we multiply it by how long the string is divided by 2 without remainder
    # 
    roundedDown = (n // len(s))
    finalNum = countStart * roundedDown
    print("The letter a appears in this string ", finalNum)

    remainingLetters = n % len(s)

    # calculates remaining letters
    for x in range(0, remainingLetters):
        if s[x] == "a":
            finalNum += 1

    return finalNum



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
