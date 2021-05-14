n,i,j=map(int,input().split())
n1,new,n2,c=1,0,n,0
while n:
    r=n%10
    n=n//10
    c+=1
r,c=0,c-1
while c!=-1 or n2!=0:
    r=n2//pow(10,c)
    n2=n2%pow(10,c)
    c-=1
    if r%i==0:
        r=j
        if j==9:
            j=0
        j+=1
    new=new*10+r
    n1=n1*10
print(new)
