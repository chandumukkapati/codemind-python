def prime(n):
    if n==1:
        return 0
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    else:
        return 1
def rev(n):
    re=0
    while(n>0):
        r=n%10
        n=n//10
        re=re*10+r
    return re
        
n=int(input())
if prime(n)==0:
    print("not prime")
else:
    if prime(n)==1 and prime(rev(n))==1:
        print("circular prime")
    else:
        print("prime but not a circular prime")
                    
