def movezeros(n,d):
    for i in d:
        if i==0:
            d.insert(n,0)
            d.remove(0)
    print(d)

n=int(input())
data=list(map(int,input().split()))
movezeros(n,data)
print(*data)
