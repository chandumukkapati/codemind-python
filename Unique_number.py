n=int(input())
a=[]
while(n>0):
    r=n%10
    n=n//10
    a.append(r)
for i in a:
    if a.count(i)!=1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")
    

        
