def max_1(n,d):
    c,x=0,0
    for i in range(len(d)-1):
        if d[i]==1 and d[i+1]==1:
            x+=1
        elif d[i]==1 and d[i+1]!=1:
            x+=1
        else:
            if c<x:
                c=x
            x=0
    x+=1
    if c<x:
        return x
    return c

n=int(input())
data=list(map(int,input().split()))
print(max_1(n,data))
