def leader(n,d):
    l=[]
    for i in range(n):
        if d[i]==max(d[i:]):
            l.append(d[i])
    return l
n=int(input())
d=list(map(int,input().split()))
print(*leader(n,d))
