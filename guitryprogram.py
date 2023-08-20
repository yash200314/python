from tkinter import *
root = Tk()

def date():
    day = int(input_1.get())
    month=int(input_2.get())
    year =int(input_3.get())



root.title("year calculate:")
root.geometry("200x100")

input_1=Label(root,text="Day")
input_1=Entry(root)

input_2=Label(root,text="Month")
input_2=Entry(root)

input_3=Label(root,text="Year")
input_3=Entry(root)

input_1.grid(row=0,column=0)
input_1.grid(row=0,column=1)

input_2.grid(row=1,column=0)
input_2.grid(row=1,column=3)


root.mainloop()