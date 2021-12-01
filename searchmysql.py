from tkinter import*
import pymysql
import pymysql.cursors
from tkinter import messagebox

def find():
    uid=mid.get()
    conn=pymysql.connect(host='Localhost',user='root',password='',db='hp')
    a=conn.cursor()

    a.execute("select *from mak where   id='"+uid+"'")
    results=a.fetchall()
    count=a.rowcount
    print(count)
    print(results)
    print(count)
    if(count>0):
        for row in results:
            iid.set(row[0])
            name.set(row[1])
            address.set(row[2])
            salary.set(row[3])
        
    else:
        messagebox.showinfo("hello","Record not found")




win=Tk()
win.title("mysqldatabase")
win.geometry("600x400")
win.resizable(False,False)

mid=StringVar()
iid=StringVar()
name=StringVar()
address=StringVar()
salary=StringVar()

lb1=Label(win,text="ID",font=("arial",20,"bold")).grid(row=0,column=0)
txt1=Entry(win,textvariable=mid,bg="powder blue",fg="black",justify="right",bd=5).grid(row=0,column=1)

btn=Button(win,text="SUBMIT",font=("halvatica",10),relief=GROOVE,bd=5,bg="red",fg="black",command=find).grid(row=1,column=1)

lb1=Label(win,text="ID",font=("arial",20,"bold")).grid(row=2,column=0)
txt1=Entry(win,textvariable=iid,bg="powder blue",fg="black",justify="right",bd=5).grid(row=2,column=1)


lb1=Label(win,text="NAME",font=("arial",20,"bold")).grid(row=3,column=0)
txt1=Entry(win,textvariable=name,bg="powder blue",fg="black",justify="right",bd=5).grid(row=3,column=1)

lb1=Label(win,text="ADDRESS",font=("arial",20,"bold")).grid(row=4,column=0)
txt1=Entry(win,textvariable=address,bg="powder blue",fg="black",justify="right",bd=5).grid(row=4,column=1)

lb1=Label(win,text="SALARY",font=("arial",20,"bold")).grid(row=5,column=0)
txt1=Entry(win,textvariable=salary,bg="powder blue",fg="black",justify="right",bd=5).grid(row=5,column=1)


