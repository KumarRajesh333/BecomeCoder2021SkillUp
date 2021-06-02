def sumofdigits(data,n):
    for i in range(n):
        s=0
        while data[i]:
            r,data[i]=data[i]%10,data[i]//10
            s=s+r
        data[i]=s
            
n=int(input())
data=list(map(int,input().split()))
sumofdigits(data,n)
print(*data)
