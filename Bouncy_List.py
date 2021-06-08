def bouncy(n,d):
    i=0
    if d[0]<d[1]:
        l,h='low','high'
        while i<n-1:
            if i%2:
                if d[i]<=d[i+1]:
                    return False
            else:
                if d[i]>=d[i+1]:
                    return False
            i+=1 
    else:
        l,h,i='low','high',1
        while i<n-1:
            if i%2:
                if d[i]>=d[i+1]:
                    return False
            else:
                if d[i]<=d[i+1]:
                    return False
            i+=1 
    return True
 
n=int(input())
data=list(map(int,input().split()))
print(bouncy(n,data))
