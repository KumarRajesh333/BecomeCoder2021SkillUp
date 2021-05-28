n=int(input())
for i in range(n):
    for j in range(n):
        if i%2:
            print(n-j,end='')
            continue
        print(j+1,end='')
    print()
