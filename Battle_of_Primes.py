def prime(n):
    if n==1:
        return 0
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
m=int(input())
s=n+m
for i in range(s+1,999999):
    if prime(i):
        c=i
        break
k=c-s
print(k)
        