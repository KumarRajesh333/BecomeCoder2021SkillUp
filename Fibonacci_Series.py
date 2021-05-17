cube = lambda x: pow(x,3)# complete the lambda function 

def fibonacci(n):
    l,a,b=[],0,1
    if n==0:
        return []
    if n==1:
        l.append(0)
        return l
    while n!=2:
        k=b+a
        a=b
        b=k
        l.append(k)
        n-=1
    else :
        l.insert(0,0)
        l.insert(1,1)
        return l
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
