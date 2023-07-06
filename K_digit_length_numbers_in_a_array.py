import math
n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if(i<0):
        i=abs(i)
    if(i!=0):
        d=int(math.log10(i)+1)
    else:
        d=1
            
    if (d==m):
        c+=1
print(c)    