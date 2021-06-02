def palindrome(data,n):
    c=0
    for i in range(n):
        s,x=0,data[i]
        while data[i]:
            r,data[i]=data[i]%10,data[i]//10
            s=s*10+r
        data[i]=s
        if x==s:
            c+=1
    return c

n=int(input())
data=list(map(int,input().split()))
print(palindrome(data,n))
