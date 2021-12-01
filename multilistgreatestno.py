li=[[0,0,0],[0,0,0],[0,0,0]]
print("enter the 9 numbers")
for i in range(3):
    for j in range(3):
        n=int(input())
        li[i][j]=n
        if(li[i][j]>li[0][0]):
            li[0][0]=li[i][j]



print("your list value is")
for i in range(3):
    for j in range(3):
        print(li[i][j],end=" ")
    print()

print("greatest no is:",li[0][0])
