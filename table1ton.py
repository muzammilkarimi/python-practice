a=int(input("enter the last number"))
for i in range(1,11,1):
    for j in range(1,a+1,1):
        print(i*j,end="\t")
    print()
