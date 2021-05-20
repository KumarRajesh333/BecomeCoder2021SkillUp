def perfect(n,i=1,s=0):
    if i<n:
        if n%i==0:
            s=s+i
        perfect(n,i+1,s)
    else:
        if n==s:
            print('perfect number')
        else:
            print('not a perfect number')

n=int(input())
perfect(n)
