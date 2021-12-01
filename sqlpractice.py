from tkinter import*


win=Tk()
win.title("sql practice")







id=StringVar()
name=StringVar()
add=StringVar()
sal=StringVar()

 


lb1=Label(win,text="ID",font=("arial",20,"bold")).grid(row=0,column=0)
txt1=Entry(win,textvariable=id,bg="powder blue",fg="black",justify="right",bd=5).grid(row=0,column=1)

lb1=Label(win,text="NAME",font=("arial",20,"bold")).grid(row=1,column=0)
txt1=Entry(win,textvariable=name,bg="powder blue",fg="black",justify="right",bd=5).grid(row=1,column=1)


lb1=Label(win,text="ADDRESS",font=("arial",20,"bold")).grid(row=2,column=0)
txt1=Entry(win,textvariable=add,bg="powder blue",fg="black",justify="right",bd=5).grid(row=2,column=1)

lb1=Label(win,text="SALARY",font=("arial",20,"bold")).grid(row=3,column=0)
txt1=Entry(win,textvariable=sal,bg="powder blue",fg="black",justify="right",bd=5).grid(row=3,column=1)

btn=Button(win,text="SUBMIT",font=("halvatica",20),relief=GROOVE,bd=5,bg="red",fg="black").grid(row=4,column=1)
