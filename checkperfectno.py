a=int(input("enter the number"))
p=0
i=1

while(i<a):
    if(a%i==0):
        p=p+i
    i=i+1
if(p==a):
    print("no is perfect no:")
else:
    print("no is not perfect no:")
