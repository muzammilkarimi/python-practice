from tkinter import*
import pymysql
import pymysql.cursors


def insert():
    uid=iid.get()
    salary=sal.get()

    try:
        conn= pymysql.connect(host='localhost',user='root',password='',db='hp')
        a=conn.cursor()
        a.execute("update mak set salary=salary+('"+salary+"')where id=('"+uid+"')")
        conn.commit()
        print('update')
    except:
        conn.rollback()
        print('not update')
    conn.close()


win=Tk()
win.title("mysqldatabase")
win.geometry("600x400")
win.resizable(False,False)

iid=StringVar()
sal=StringVar()

lb1=Label(win,text="ID",font=("arial",20,"bold")).grid(row=0,column=0)
txt1=Entry(win,textvariable=iid,bg="powder blue",fg="black",justify="right",bd=5).grid(row=0,column=1)

lb1=Label(win,text="salary",font=("arial",20,"bold")).grid(row=1,column=0)
txt1=Entry(win,textvariable=sal,bg="powder blue",fg="black",justify="right",bd=5).grid(row=1,column=1)



btn=Button(win,text="UPDATE",font=("halvatica",20),relief=GROOVE,bd=5,bg="red",fg="black",command=insert).grid(row=2,column=1)

