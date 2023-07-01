n=input()
n=n.lower()
c=0
s="abcdefghijklmnopqrstuvwxyz1234567890 "
for i in n:
    if i not in s:
        c+=1
print(c)        
        