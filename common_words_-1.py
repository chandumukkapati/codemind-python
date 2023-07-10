n1=input().lower().split()
n2=input().lower().split()
c=0
for i in n1:
    if i in n2:
        c+=1
print(c)        