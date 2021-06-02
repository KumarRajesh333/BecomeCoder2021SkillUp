import math as m
def countPrime(data):
    p,np=[],[]
    for i in data:
        s=0
        if i==1:
            s=1
        for j in range(2,int(m.sqrt(i))+1):
            if i%j==0:
                s+=1
                break
        if s==0:
            p.append(i)
        else:
            np.append(i)
    return p,np

x,y=countPrime(list(map(int,input().split())))
print(*x)
print(*y)
