#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    # for every unique element in the socks
    for element in set(ar):
        # count how many there are, divide by 2 but remove decimals
        # so if there is 3 socks, that goes down to 1.5. // removes the .5, meaning it goes down to 1 pair.
        pairs += (ar.count(element) // 2)

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
