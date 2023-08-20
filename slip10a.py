from tkinter import*
from tkinter import messagebox
root=Tk()
def click():
    messagebox.showinfo("alert")

root.geometry("300x300")
root.title("alert button")
btn=Button(root,text="click here",command=click).pack()
root.mainloop()