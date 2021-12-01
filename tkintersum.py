from tkinter import*

def add():
    a=int(num1.get())
    b=int(num2.get())
    s=a*b
    res.set(s)



win=Tk()

win.title("win apps")
win.geometry("400x400")
win.config(bg="blue")
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
res=StringVar()
tb3=Entry(win,textvariable=res)
tb3.grid(row=2,column=1)

btn=Button(win,text="mul",command=add)
btn.grid(row=3,column=1)
