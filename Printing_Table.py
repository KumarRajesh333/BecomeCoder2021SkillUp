n,r1,r2=map(int,input().split())  
if r1>r2:
    r=r1-r2
else:
    r=r2-r1
for i in range(r+1):
    if r1<=r2:
        print(n,"X",r1,"=",n*r1)
        r1+=1
    else:
        print(n,"X",r1,"=",n*r1)
        r1-=1
while r1!=r2:
    print(n,"X",r1,"=",n*r1)
    if r2>=r1:
        r1+=1
    else:
        r1-=1
else:
    print(n,"X",r1,"=",n*r1)
