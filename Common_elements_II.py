n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=[]
for i in l1:
    if i not in l2:
        c.append(i)
for j in l2:
    if j not in l1:
        c.append(j)
print(*c)        