data={}
for i in range(0,3):
    print("enter the user no:")
    k=input()
    data[k]={}
    print("enter user ID:-")
    idd=input()
    print("enter the user name:-")
    n=input()
    print("enter the user address:-")
    a=input()
    data[k]['ID']=idd
    data[k]['name']=n
    data[k]['address']=a
print(data)
