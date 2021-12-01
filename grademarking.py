print("calculate grade")
a=int(input("1--subj"))
b=int(input("2--subj"))
c=int(input("3--subj"))
d=int(input("4--subj"))
e=a+b+c+d
e=e/4
if(e>90 and e<=100):
    print(" A grade ")
elif(e<=90 and e>80):
    print(" B grade ")
elif(e<=80 and e>70):
    print(" C grade ")
elif(e<=70 and e>60):
    print(" D grade ")
else:
    print("FAIL")
print(e,"%")
