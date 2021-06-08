def sorting(n,d):
    c1,c2,x=1,0,0
    for i in range(1,len(d)):
        if d[i-1]<d[i]:
            c2,c1=0,c1+1
        elif d[i-1]==d[i]:
            c1,c2=c1+1,c2+1
        else:
            c2+=1
            if c1>c2 and x<c1:
                x=c1
            elif c2>c1 and (x<c2 or x<c1):
                x=c2
            c1=1
    if x<c1:
        return c1
    return x

n=int(input())
data=list(map(int,input().split()))
print(sorting(n,data))
