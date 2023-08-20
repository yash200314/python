from tkinter import *

#pack() example


parent = Tk()
rb=Button(parent,text="Red" ,fg='red',activeforeground="blue")
rb.pack(expand=True)
gb=Button(parent,text="Black",fg='orange')
gb.pack(side=TOP)
parent.mainloop()