n=input().split()
s=[]
for i in range(len(n)-1,-1,-1):
    s.append(n[i][::-1])
print(*s)        