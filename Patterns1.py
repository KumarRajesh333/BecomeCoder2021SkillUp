#cube = lambda x: pow(x,3)# complete the lambda function 

def fibonacci(n,r):
    for i in range(n,r):
        print(n,r,i)
        l,a,b=[],0,1
        if i==0:
            continue
        if i==1:
            l.append(0)
        while i!=2:
            k=b+a
            a=b
            b=k
            l.append(k)
            i-=1
        else :
            l.insert(0,0)
            l.insert(1,1)
    # return a list of fibonacci numbers
    return l
if __name__ == '__main__':
    n,r = map(int,input().split())
    print(n,r)
    print(list(map(int, fibonacci(n,r))))
