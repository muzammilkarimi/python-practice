print("enter any 10 numbers")
s=0
for i in range(1,11,1):
    n=int(input())
    if(n%3==0 and n%5==0):
        s=s+n
print("sum of the no:",s)
      
