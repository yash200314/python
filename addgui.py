import tkinter as tk

def sub():
    num1 = float(input_1.get())
    num2 = float(input_2.get())
    Result = num2 - num1
    print("sub",Result)
    res_label.config(text=Result)

root=tk.Tk()
root.title("--sub of two number--")
label_1=tk.Label(root, text="num1")
input_1=tk.Entry(root)
label_2=tk.Label(root,text="num2")
input_2=tk.Entry(root)
sub_btn=tk.Button(root,text="sub",command=sub)

res_label = tk.Label(root , text="result")

label_1.grid(row=0 , column=0)
input_1.grid(row=0 , column=1)
label_2.grid(row=1 , column=0)
input_2.grid(row=1 , column=1)
sub_btn.grid(row=2 , column=0 , columnspan=2)
res_label.grid(row=3 , column=0 , columnspan=2)
root.mainloop()