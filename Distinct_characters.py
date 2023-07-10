n=input().lower()
s=list(set(n))
if(" " in s):
    s.remove(" ")
s=sorted(s)
print("".join(s),end="")    
    