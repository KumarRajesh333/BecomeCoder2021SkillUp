n=int(input())
while True:
    print(n,end=' ')
    if n==1:
        break
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
        
           # or
'''          
def seq(n):
    if n%2:
        return 3*n+1
    return n//2

n=int(input())
print(n,end=' ')
while(n):
    n=seq(n)
    print(n,end=' ')
    if n==1:
        break

            or

def seq(n):
    print(n,end=' ')
    if n==1:
        return 
    if n%2==0:
        seq(n//2)
    else:
        seq(3*n+1)

n=int(input())
seq(n)
'''
