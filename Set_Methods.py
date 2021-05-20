n = int(input())
s = set(map(int, input().split()))
n2 = int(input())
for i in range(n2):
    s2 = input().split()
    if s2[0]=="pop":
        s.pop()
    elif s2[0]=='remove':
        s.remove(int(s2[1]))
    else:
        s.discard(int(s2[1]))
print(sum(s))
