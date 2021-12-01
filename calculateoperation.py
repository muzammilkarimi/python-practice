print("calculate operation")
print("1 --sum")
print("2--sub")
print("3--div")
print("4--mul")
ch=int(input("enter your choice"))
a=int(input("enter the number of a"))
b=int(input("enter the number of b"))
if(ch==1):
    print("sum of the number",a+b)
elif(ch==2):
    print("sub of numbers",a-b)
elif(ch==3):
    print("division of number",a/b)
elif(ch==4):
    print("mul of the number",a*b)
else:
    print("wrong choice")   
            
