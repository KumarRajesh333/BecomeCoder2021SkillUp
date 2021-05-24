from math import *
def pronic(n):
    m=int(sqrt(n))
    if n==m*(m+1):
        return "True"
    else:
        return 'False'

n=int(input())
print(pronic(n))
