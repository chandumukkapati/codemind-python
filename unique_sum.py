n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(len(l)):
    if l[i]==-1:
        continue
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            l[j]=-1
for i in l:
    if i!=-1:
        s+=i
print(s)        