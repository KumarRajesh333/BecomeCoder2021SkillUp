def harshad(n,t,s=0):
    if n:
        r=n%10
        return harshad(n//10,t,s+r)
    if t%s!=0:
        return 'False'
    else:
        return 'True'
n=int(input())
t=n
print(harshad(n,t))
