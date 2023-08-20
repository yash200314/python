from tkinter import*
root=Tk()
lb1=Listbox(root,fg='yellow',bg='gray',activestyle="dotbox",bd=1)
label=Label(root,text="Computer Science Course").pack()
lb1.insert(1,"Data Structure and algorithm")
lb1.insert(2,"Python")
lb1.insert(3,"Software")
lb1.pack()
root.mainloop()