def min_max(n,data):
    a,b=data[0],data[0]
    for i in data:
        if i>b:
            b=i
        if i<a:
            a=i
    return a,b

n=int(input())
data=list(map(int,input().split()))
mi,ma=min_max(n,data)
print(mi,ma)
