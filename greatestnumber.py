print(" Greatest Number ")
a=int(input("A--no: "))
b=int(input("B--no: "))
c=int(input("C--no: "))

if(a>b):
    if(a>c):
        print(" A is greatest number: ",a)
    elif(a<c):
        print(" C is greatest number: ",c)
elif(b>a):
    if(b>c):
        print(" B is greatest number: ",b)
    
