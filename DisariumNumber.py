'''def disarium(n):
    t,p,s=n,0,0
    while t:
        t=t//10
        p+=1
    while n:
        r=n%10
        n=n//10
        s=s+pow(r,p)
        p-=1
    return s
n=int(input())
print(disarium(n)==n)
'''

def disarium(n,p,s=0):
    if n:
        r=n%10
        s=s+pow(r,p)
        return disarium(n//10,p-1,s)
    return s
        
n=int(input())
t,p=n,0
while t:
    t=t//10
    p+=1
print(disarium(n,p)==n)
