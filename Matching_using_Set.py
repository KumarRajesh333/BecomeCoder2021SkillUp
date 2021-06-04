def original(data):
    c=0
    d=list(set(data))
    for j in range(len(d)):
        if d[j]==data[j]:
            c+=1
    return c
print(original(list(map(int,input().split()))))
