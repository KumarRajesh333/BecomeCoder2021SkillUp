def mul(a,b,ans):
    if a==0:
        print(ans)
        return
    if a%2!=0:
        ans+=b
    mul(a//2,b*2,ans)
    
a,b=map(int,input().split())
mul(a,b,ans=0)
        
        ##or
'''
  
a,b=map(int,input().split())
s=0
while a:
    if a%2:
        s+=b
    a=a//2
    b=b*2
print(s)

'''
