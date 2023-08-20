from tkinter import *

#grid() example

from tkinter import *
parent=Tk()
name=Label(parent,text='name').grid(row=0,column=0)
e1=Entry(parent).grid(row=0,column=1)

roll=Label(parent,text='rollno').grid(row=2,column=0)
e2=Entry(parent).grid(row=2,column=1)

addr=Label(parent,text='addr').grid(row=3,column=0)
e3=Entry(parent).grid(row=3,column=1)

parent.mainloop()
