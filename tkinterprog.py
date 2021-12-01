from tkinter import*
from tkinter import messagebox

def fun1():
    messagebox.showinfo("hello","its working")
    child=Tk()
    child.geometry("700x700")

win=Tk()
win.geometry("700x700")
menu1=Menu(win)
win.config(menu=menu1)

subMenu1=Menu(menu1)
menu1.add_cascade(label="file",menu=subMenu1)

subMenu1.add_command(label="new project...",command=fun1)
subMenu1.add_command(label="new...",command=fun1)

editMenu=Menu(menu1)
menu1.add_cascade(label="edit",menu=editMenu)
editMenu.add_command(label="new project",command=fun1)
