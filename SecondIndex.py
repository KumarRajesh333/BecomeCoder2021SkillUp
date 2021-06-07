def secondindex(data,s):
    dic,j,re={},0,0
    if s in data:
        x=data.count(s)
        if x>1:
            for i in data:
                if i==s:
                    data.remove(s)
                    j+=1
                    if j==1:
                        re=data.index(i)+j
        else:
            return 'Only one time'
        return re
    else:
        return False
n=int(input())
data=list(map(int,input().split()))
s=int(input())
print(secondindex(data,s))
