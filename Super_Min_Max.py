def super_min_max(d,ma,mi,j=0):
    mar,mir=ma,mi
    for i in d:
        if i<mi:
            mi=i
        if ma<i:
            ma=i
    j+=1
    if j==2:
        l=[]
        if mi==mir:
            l.append('Super min &')
        else:
            l.append('Not super min &')
        if ma==mar:
            l.append('Super max')
        else:
            l.append('Not super max')
        return l
    return ma,mi
def reverse(ma,mi):
    mar,mir=0,0
    while ma!=0:
        r1,ma=ma%10,ma//10
        mar=mar*10+r1
    while mi!=0:
        r2,mi=mi%10,mi//10
        mir=mir*10+r2
    return mar,mir
    
d=list(map(int,input().split()))
ma,mi=d[0],d[0]
ma,mi=super_min_max(d,ma,mi)
d.remove(ma)
d.remove(mi)
mar,mir=reverse(ma,mi)
x=super_min_max(d,mar,mir,j=1)
print(*x)
