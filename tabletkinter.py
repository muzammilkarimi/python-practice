from tkinter import*

def add():
    print("\n")
    y=10
    for x in range(1,11):
        m=int(num.get())
        print('\t\t',(x),'x',(m),'m',(x*m),)
        y=y+1
        L1=Label(win,text=str(m)+'X'+str(x)+'='+str(x*m)).grid(row=y,column=7)



win=Tk()

win.title("win apps")
win.geometry("400x400")
win.config(bg="blue")
win.resizable(False,False)

L1=Label(win,text="number")
L1.grid(row=1,column=6)
num=StringVar()
tb1=Entry(win,textvariable=num)
tb1.grid(row=3,column=6)




btn=Button(win,text="table",command=add)
btn.grid(row=5,column=6)



