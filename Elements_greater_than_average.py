n=int(input())
l=list(map(int,input().split()))
s=sum(l)
c=0
avg=s//n
for i in l:
    if i>=avg:
        c+=1
print(c)        