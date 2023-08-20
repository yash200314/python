import time 
from tkinter import*
def clock():
    time_val=time.strftime("%H:%M:%S")
    Label.configure(text=time_val)
    Label.after(100,clock)

root=Tk()
root.title("Clock")
root.geometry("200x300")
Label=Label(root,bg="blue",fg="yellow",font=("arial",18,"bold"))
Label.grid(row=0,column=1)
clock()
root.mainloop()