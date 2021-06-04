def original(data):
    for i in data:
        if d1.count(i)==0:
            d1.append(i)
		return d1
d1=[]  
print(*original(list(map(int,input().split())))) 
