#cube = lambda x: pow(x,3)# complete the lambda function 

def fibonacci(n,r):
    a,b=0,1
    if n==0:
        print(0,1,end=' ')
    if n==1:
        print(1,end=' ')
    k=0
    while k<=r:
        k=b+a
        a=b
        b=k
        if k>=n and k<=r:
            print(k,end=' ')
    # return a list of fibonacci numbers
if __name__ == '__main__':
    n,r= map(int,input().split())
    fibonacci(n,r)
