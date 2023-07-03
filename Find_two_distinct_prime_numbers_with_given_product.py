def prime(n):
    for i in range(2,n//2):
        if n%i==0 or n==1:
            return 0
    else:
         return 1   


n=int(input())
for i in range(2,n//2+1):
    if prime(i)==1:
        if n%i==0 and prime(n//i)==1:
            print(i,n//i)
            break
else:
    print("-1")