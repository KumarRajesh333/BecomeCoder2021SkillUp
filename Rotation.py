def rotation(n,d,r):
    r=r%n
    for i in range(r):
        x=d[0]
        for j in range(1,len(d)):
            d[j-1]=d[j]
        d[j]=x
    return d
  
n=int(input())
d=list(map(int,input().split()))
r=int(input())
print(*rotation(n,d,r))
