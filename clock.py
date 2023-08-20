import time
from tkinter import*
def clock():
    time_val=time.strftime("%H:%M:%S")
    Label.config(text=time_val)
    Label.after(100,clock)

root=Tk()
root.title("Digital clock")
Label=Label(root,fg="green",bg="yellow",justify=CENTER)
Label.grid(row=3,column=7)
clock()
root.mainloop()