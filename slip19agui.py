import tkinter as tk

def mul():
    num1=float(input_1.get())
    num2=float(input_2.get())
    Result=num1*num2
    print("Result",Result)
    res_label.config(text=Result)
    git add README.md

root=tk.Tk()
root.title("Multiplication of number")

label_1=tk.Label(root,text="num1")
input_1=tk.Entry(root)

label_2 = tk.Label(root , text="num2")
input_2 = tk.Entry(root)

mul_button=tk.Button(root,text="mul",command=mul)
res_label=tk.Label(root , text="result")

label_1.grid(row=0 , column=0)
input_1.grid(row=0 , column=1)
label_2.grid(row=1 , column=0)
input_2.grid(row=1 , column=1)
mul_button.grid(row=2 , column=0 , columnspan=2)
res_label.grid(row=3 , column=0 , columnspan=2)

root.mainloop()

