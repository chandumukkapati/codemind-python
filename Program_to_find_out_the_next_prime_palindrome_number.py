def prime(n):
    if n==1:
        return 0
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    else:
        return 1
def pal(n):
    re=0
    temp=n
    while(n>0):
        r=n%10
        n=n//10
        re=re*10+r
    if(temp==re):
        return 1
    else:
        return 0
n=int(input())
for i in range(n+1,100000000):
    if prime(i)==1 and pal(i)==1:
        print(i)
        break