def sort_order(n,data):
    x=data.copy()
    x.sort()
    for i in range(len(data)):
        if data[i]==x[i]:
            pass
        elif data[i]==x[n-1]:
            n-=1
            pass
        else:
            return False
    return True
    
n=int(input())
data=list(map(int,input().split()))
print(sort_order(n,data))
