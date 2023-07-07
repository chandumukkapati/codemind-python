n=input()
v="aeiouAEIOU"
s=[]
for i in n:
    if i in v and i not in s:
        s.append(i)
print(*s)        