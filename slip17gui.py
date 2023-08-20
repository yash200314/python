from tkinter import*
root=Tk()
root.geometry("400x400")

def size():
    text.config(font=("arial",80))
    text.config(bg="gray",fg="yellow")

def size1():
    text.config(font=("times new roman",50))
    text.config(bg="yellow",fg="red")

text=Label(root,text="jai hind jai bharat")
text.pack()
frame=Frame(root)
Label(frame,text="select the color:").pack()

button=Checkbutton(root,text="click here",command=size).pack()
button1=Checkbutton(root,text="click here",command=size1).pack()

root.mainloop()