def original(data):
    c1=0
    for i in data:
        if d1.count(i)==0:
            d1.append(i)
    for j in range(len(d1)):
        if d1[j]==data[j]:
            c1+=1
    print(d1)
    return c1
d1=[]  
print(original(list(map(int,input().split()))))
