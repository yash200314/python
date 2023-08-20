from tkinter import*
root=Tk()
def change():
    newval=value.get()
    root.config(background=newval)

root.config(background="gray")
root.geometry("500x500")
root.title("color change")
color=Label(root,text="color",fg="orange",bg="white")
color.grid(row=1,column=1)
value=Entry(root)
value.grid(row=1,column=3)
apply=Button(root,text="apply color",fg="green",bg="black",command=change)
apply.grid(row=1,column=5)
root.mainloop()
