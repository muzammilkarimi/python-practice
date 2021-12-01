from tkinter import*

def add():
    bsalery=int(bsalery.get())
    ta=bsalery*2/100
    da=bsalery*2/100
    hra=bsalery*3/100
    tsalery=bsalery+ta+da+hra
    tsalery.set(tsalery)
    itax=tsalery/100*2
    nsalery=tsalery-itax
    nsalery.set(nsalery)
    
    
   



win=Tk()

win.title("win apps")
win.geometry("800x800")
win.config(bg="black")
win.resizable(False,False)

L1=Label(win,text="basic salery")
L1.grid(row=0,column=0)
bsalery=StringVar()
tb1=Entry(win,textvariable=bsalery)
tb1.grid(row=0,column=1)

L1=Label(win,text="TA")
L1.grid(row=1,column=0)
ta=StringVar()
tb1=Entry(win,textvariable=ta)
tb1.grid(row=1,column=1)

L1=Label(win,text="  DA      ")
L1.grid(row=2,column=0)
da=StringVar()
tb1=Entry(win,textvariable=da)
tb1.grid(row=2,column=1)

L1=Label(win,text="  HRA  ")
L1.grid(row=3,column=0)
hra=StringVar()
tb1=Entry(win,textvariable=hra)
tb1.grid(row=3,column=1)

L1=Label(win,text="itax")
L1.grid(row=4,column=0)
itax=StringVar()
tb1=Entry(win,textvariable=itax)
tb1.grid(row=4,column=1)

L1=Label(win,text="total salery")
L1.grid(row=5,column=0)
tsalery=StringVar()
tb1=Entry(win,textvariable=tsalery)
tb1.grid(row=5,column=1)

L1=Label(win,text="net salery")
L1.grid(row=6,column=0)
nsalery=StringVar()
tb1=Entry(win,textvariable=nsalery)
tb1.grid(row=6,column=1)

btn=Button(win,text="result",command=add)
btn.grid(row=7,column=1)



