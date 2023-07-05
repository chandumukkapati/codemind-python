n=int(input())
l=list(map(int,input().split()))
s=[]
c=[]
for i in l:
    if i not in s:
        s.append(i)
        c.append(l.count(i))
for i in range(len(s)):
    print(s[i],c[i],end=" ")