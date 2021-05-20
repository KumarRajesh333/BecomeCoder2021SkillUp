x,r=map(int,input().split())
l,l2,j,k=[],[],0,0
for i in range(x+1):
    l.append((x-i+1)*" "+(2*i-1)*"*"+(x-i+1)*" ")
for i in range(x-1,0,-1):
    l2.append((x-i+1)*" "+(2*i-1)*"*"+(x-i+1)*" ")
for i in l:
    print(i*r)
for i in l2:
    print(i*r)
