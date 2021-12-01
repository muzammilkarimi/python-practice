from tkinter import*

def sub():
    m=int(num4.get())
    n=int(num1.get())
    o=int(num2.get())

    if (m==1):
        s=(n+o)
        num3.set(s)
    elif (m==2):
        s=(n-o)
        num3.set(s)
    elif (m==3):
        s=(n*o)
        num3.set(s)
    elif (m==4):
        s=(n/o)
        num3.set(s)
    else:
        print("this operation is invalid")
    



win=Tk()

win.title("win apps")
win.geometry("400x400")
win.config(bg="black")
win.resizable(False,False)

L1=Label(win,text="number1")
L1.grid(row=0,column=0)
num1=StringVar()
tb1=Entry(win,textvariable=num1)
tb1.grid(row=0,column=1)

L2=Label(win,text="number2")
L2.grid(row=1,column=0)
num2=StringVar()
tb2=Entry(win,textvariable=num2)
tb2.grid(row=1,column=1)


L3=Label(win,text="result")
L3.grid(row=2,column=0)
num3=StringVar()
tb3=Entry(win,textvariable=num3)
tb3.grid(row=2,column=1)


L3=Label(win,text="Enter choice")
L3.grid(row=0,column=2)
num4=StringVar()
tb3=Entry(win,textvariable=num4)
tb3.grid(row=0,column=3)


btn=Button(win,text="submit",command=sub)
btn.grid(row=5,column=0)

