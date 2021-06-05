def mincount(l):
    i,x,r=0,[],[]
    while i<len(l):
        x.append(l.count(l[i]))
        i+=1
    a,i=min(x),0
    while i<len(l):
        if a==(l.count(l[i])) and l[i] not in r:
            r.append(l[i])
        i=i+1
    return r  
l=list(map(int,input().split()))
print(*mincount(l))
