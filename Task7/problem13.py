# 13
# Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


from collections import Counter

def isValid(s):
    freq = Counter(s)
    counts = Counter(freq.values())

    if len(counts) == 1:
        return "YES"

    if len(counts) > 2:
        return "NO"

    f1, f2 = counts.keys()
    c1, c2 = counts.values()

    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        return "YES"

    if abs(f1 - f2) == 1 and (c1 == 1 or c2 == 1):
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
