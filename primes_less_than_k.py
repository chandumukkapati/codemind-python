def prime(n):
    if n==1:
        return 0
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
l=list(map(int,input().split()))
m=int(input())
c=0
for i in l:
    if i<=m and prime(i):
        c+=1
print(c)        