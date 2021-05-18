def position_of_fib(n):
    a,b,s=0,1,2
    while True:
        if n==0:
            return 1
        if n==1:
            return (2,3)
        c=a+b
        s+=1
        a,b=b,c
        if c==n:
            return s
        if c>n:
            return 'False'

n=int(input())
print(position_of_fib(n))
