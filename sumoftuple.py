l=[]
i=0
s=0
for i in range(10):
    print("enter the number")
    a=int(input())
    l.insert(i,a)
    i=i+1
    s=s+l[i]
tp=tuple(l)
print(tp,"=",s)




