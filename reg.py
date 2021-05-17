#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    l=[]
    for i in range(len(a)):
        if a.count(a[i]) not in l:
            l.append(a.count(a[i]))
    return 0
if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(result)
