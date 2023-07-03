def prime(n):
    if n < 2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
l=[]
temp = n
c=0
while temp:
    r=temp%10
    temp=temp//10
    l.append(r)
for i in l:
    if prime(i)==1:
        c+=1
    
if c == len(l) and prime(n)==1:
    print("Mega Prime")
else:
    print("Not Mega Prime")
    
