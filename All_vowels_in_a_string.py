n=input()
v="aeiou"
s=[]
for i in n:
    if i in v and i not in s:
        s.append(i)
if(len(s)==len(v)):
    print("True")
else:
    print("False")