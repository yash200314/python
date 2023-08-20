from tkinter import*
def demo():
    print('eat')

parent=Tk()
parent.geometry('100x100')
btn=Button(parent,text="click here!!!",bd='100',fg='blue',state='active',width='200',relief=GROOVE,activeforeground='red')
btn1=Button(parent,text="click here!!!",bd='100',fg='blue',state='active',width='200')
btn2=Button(parent,text="click here!!!",bd='100',fg='blue',state='active',command=demo)
#btn1.pack()
#btn.pack()
btn2.pack()

parent.mainloop()