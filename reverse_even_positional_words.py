n=input().split()
s=[]
for i in range(len(n)):
    if i%2!=0:
        s.append(n[i])
    else:
        s.append(n[i][::-1])
print(*s)        
    