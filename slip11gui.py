import tkinter as tk
root=tk.Tk()
def change(color): 
    root.config(bg=color)

menubar=tk.Menu(root)
color_menu=tk.Menu(menubar,tearoff=0)

color_menu.add_command(label="red",command=lambda:change("red"))
color_menu.add_command(label="green",command=lambda:change("green"))
menubar.add_cascade(label="color",menu=color_menu)
root.config(menu=menubar)
root.mainloop()