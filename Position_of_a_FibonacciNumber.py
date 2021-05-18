def isfib(n):
    a,b,x,y=0,1,0,0
    while True:
        c=a+b
        if c==n:
            print("True")
            break
        if c<n:
            x=n-c
            u=c
        else:
            y=c-n
            v=c
        if c>n:
            if x==y:
                print(u,v)
                break
            elif x<y:
                print(u)
                break
            else:
                print(v)
                break
        a,b=b,c
        
t=int(input())
for i in range(t):
    n=int(input())
    isfib(n)
