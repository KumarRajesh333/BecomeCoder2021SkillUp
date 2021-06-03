def findmin(n,data):
    a,mc=data[0],0
    for i in data:
        if i==a:
            mc+=1
        if i<a:
            a=i
            mc=1
    l=[a,mc]
    for i in range(mc):
        l.append(data.index(a)+i)
        data.remove(a)
    return l

n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(*minval)
