n=int(input())
l=list(map(int,input().split()))
m=int(input())
s=[]
for i in l:
    if l.count(i)==m and i not in s:
        s.append(i)
if(s==[]):
    print("-1")
else:
    print(*s,end=" ")
        