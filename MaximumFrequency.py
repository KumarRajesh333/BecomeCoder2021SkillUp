data=list(map(int,input().split()))
dic,m={},0
for i in data:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]+=1
    if m<dic[i]:
        m=dic[i]
for i in dic.keys():
    if m==dic[i]:
        print(i,dic[i])
