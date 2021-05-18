t=int(input())
for i in range(t):
    n=int(input())
    a,b=0,1
    while True:
        c=a+b
        if c==n:
            print("True")
            break
        if c>n:
            print("False")
            break
        a,b=b,c
