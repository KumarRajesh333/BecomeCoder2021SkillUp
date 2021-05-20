n=int(input())
s=input().split()
s=set(s)
r=int(input())
for i in range(r):
    c=input().split()
    s2=input().split()
    s2=set(s2)
    if c[0]=="intersection_update":
        s&=(s2)
    elif c[0]=="update":
        s|=(s2)
    elif c[0]=='difference_update':
        s-=(s2)
    else:
        s^=(s2)
s,l=list(s),[]
for i in range(len(s)):
    l.append(int(s[i]))
print(sum(l))
