n=int(input())
l=list(map(int,input().split()))
f=0
s=sum(l)
for i in range(n//2+1):
    f+=i
s2=s-f
print(abs(s2-f))