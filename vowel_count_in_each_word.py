n=input().split()
v="aeiou"
for i in n:
    c=0
    for j in i:
        if j in v:
            c+=1
    print(c,end=" ")        