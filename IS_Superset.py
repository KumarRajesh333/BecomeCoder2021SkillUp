s=set(map(int,input().split()))
n,r=int(input()),0
for i in range(n):
    s2=set(map(int,input().split()))
    if s.issuperset(s2):
        r+=1
if r==n:
    print("True")
else:
    print('False')
