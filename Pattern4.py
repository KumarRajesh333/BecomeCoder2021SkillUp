n=int(input())
for i in range(n):
    for j in range(n):
        if j==0:
            print(i+1,end='')
            continue
        print(j+1,end='')
    print()
