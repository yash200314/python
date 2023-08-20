import tkinter as tk
from tkinter import font

def change():
    font_name=font_var.get()
    bold=bold_var.get()
    size=size_var.get()
    label.configure(font=(font_name,size,"bold" if bold else "normal"))

root=tk.Tk()
root.title("font color style change")
label=tk.Label(root,text="hello world")
label.pack(pady=20)

font_var=tk.StringVar()
bold_var=tk.BooleanVar()
size_var=tk.IntVar()

tk.Checkbutton(root,text="Font Name",variable=font_var,onvalue="Helvetica",offvalue="Arial",command= change).pack()
tk.Checkbutton(root,text="Bold Name",variable=bold_var,command= change).pack()
tk.Checkbutton(root,text="Size",variable=size_var,onvalue="24",offvalue="13",command= change).pack()
root.mainloop()