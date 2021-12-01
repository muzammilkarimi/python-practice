from tkinter import*
from tkinter import filedialog

def fun1():
    print("it working")

def browsefunc():
    filename=filedialog.askopenfilename(filetypes=(("File","*.py"),("All Files","*.*")))
    pathLabel.config(text=filename)

    
win=Tk()
win.geometry("400x500")
menu1=Menu(win)
win.config(menu=menu1)
subMenu1=Menu(menu1)

menu1.add_cascade(label="file",menu=subMenu1)
subMenu1.add_command(label="open...",command=browsefunc)
subMenu1.add_command(label="Exit...",command=quit)

editMenu=Menu(menu1)
menu1.add_cascade(label="edit",menu=editMenu)
editMenu.add_command(label="cut",command=fun1)
pathLabel=Label(win)
pathLabel.pack()
win.mainloop()
