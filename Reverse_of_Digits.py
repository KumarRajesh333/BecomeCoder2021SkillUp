def reverseofdigits(data,n):
    for i in range(n):
        s=0
        while data[i]:
            r,data[i]=data[i]%10,data[i]//10
            s=s*10+r
        data[i]=s

n=int(input())
data=list(map(int,input().split()))
reverseofdigits(data,n)
print(*data)
