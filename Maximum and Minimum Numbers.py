n=int(input())
ma,mi,mac,mic,t=n%10,n%10,0,0,n
while n:
    r=n%10
    n=n//10
    if ma<r:
        ma=r
        mac=1
    elif ma==r:
        mac+=1
    if mi>r:
        mic=1
        mi=r
    elif mi==r:
        mic+=1
print(ma,mi)
print(mic,mac)
