n=int(input())
r,c,s,t=n%10,0,0,n
while True:
    r1=n%10
    n=n//10
    c+=1
    if n<10:
        break
n=r*pow(10,c)+t%pow(10,c)-t%10+n
print(n)
