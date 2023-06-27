n,m=map(int,input().split())
m=[]
s=0
for i in range(n):
    r=list(map(int,input().split()))
    m.append(r)
    for j in r:
        s+=j
print(s)        