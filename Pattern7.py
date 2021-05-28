n=int(input())
for i in range(1,n+1):
    if i%2==0:
        t=0
    else:
        t=1
    for j in range(1,n+1):
        print(t,end='')
        if t==0:
            t=1
        else:
            t=0
    print()
