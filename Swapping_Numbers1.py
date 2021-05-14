n=int(input())
r,c,s,t=n%10,0,0,n
while True:
    r1=n%10
    n=n//10
    c+=1
    s=s*10+r1
    if n<10:
        break
print(n*10**c+s%pow(10,c-1)*10+r)
