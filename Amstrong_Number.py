def amstrong(n,s,t,re=0):
    if n:
        r=n%10
        re=re+pow(r,s)
        amstrong(n//10,s,t,re)
    else:
        if re==t:
            print('Amstrong')
        else:
            print('Not Amstrong')

n=int(input())
s,t=0,n
while n:
    n=n//10
    s+=1
n=t
amstrong(n,s,t)
