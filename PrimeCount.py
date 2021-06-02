import math as m
def countPrime(data):
    pc=0
    for i in data:
        s=0
        if i==1:
            s=1
        for j in range(2,int(m.sqrt(i))+1):
            if i%j==0:
                s+=1
                break
        if s==0:
            pc+=1
    return pc

print(countPrime(list(map(int,input().split()))))  
