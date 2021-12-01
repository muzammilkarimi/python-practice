from tkinter import*
import pymysql
import pymysql.cursors


def insert():
    uid=iid.get()
    nm=name.get()
    add=address.get()
    sal=salary.get()

    try:
        conn= pymysql.connect(host='localhost',user='root',password='',db='hp')
        a=conn.cursor()
        a.execute("insert into mak(id,name,address,salary)values('"+uid+"','"+nm+"','"+add+"','"+sal+"')")
        conn.commit()
        print('save')
    except:
        conn.rollback()
        print('not save')
    conn.close()


win=Tk()
win.title("mysqldatabase")
win.geometry("600x400")
win.resizable(False,False)


iid=StringVar()
name=StringVar()
address=StringVar()
salary=StringVar()

lb1=Label(win,text="ID",font=("arial",20,"bold")).grid(row=0,column=0)
txt1=Entry(win,textvariable=iid,bg="powder blue",fg="black",justify="right",bd=5).grid(row=0,column=1)

lb1=Label(win,text="NAME",font=("arial",20,"bold")).grid(row=1,column=0)
txt1=Entry(win,textvariable=name,bg="powder blue",fg="black",justify="right",bd=5).grid(row=1,column=1)


lb1=Label(win,text="ADDRESS",font=("arial",20,"bold")).grid(row=2,column=0)
txt1=Entry(win,textvariable=address,bg="powder blue",fg="black",justify="right",bd=5).grid(row=2,column=1)

lb1=Label(win,text="SALARY",font=("arial",20,"bold")).grid(row=3,column=0)
txt1=Entry(win,textvariable=salary,bg="powder blue",fg="black",justify="right",bd=5).grid(row=3,column=1)

btn=Button(win,text="SUBMIT",font=("halvatica",20),relief=GROOVE,bd=5,bg="red",fg="black",command=insert).grid(row=4,column=1)


