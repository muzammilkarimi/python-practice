li=[[0,0,0],[0,0,0],[0,0,0]]
print("enter the 9 numbers")
for i in range(3):
    for j in range(3):
        n=int(input())
        li[i][j]=n

print("your list value is ")
for i in range(3):
    s=0
    for j in range(3):
        s=s+li[i][j]
        print(li[i][j],end="  ")
    print("=",s)
    print()

