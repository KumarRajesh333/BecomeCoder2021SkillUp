def secondlargest(n,data):
    ma=max(data)
    c=data.count(ma)
    if c==1:
        data.remove(ma)
        return max(data)
    else:
        for i in range(c):
            data.remove(ma)
        return max(data)
        
n=int(input())
data=list(map(int,input().split()))
print(secondlargest(n,data))
