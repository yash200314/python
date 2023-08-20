import tkinter as tk
import math

def cal():
    radius=int(r_entry.get())
    height=int(h_entry.get())

    volume = math.pi * radius ** 2 * height
    surf = 2 * math.pi * radius * height +2 *math.pi*radius**2;

    surface.config(Text=f"surface area is:{surf}")
    volumee.config(text=f"volume is:{volume}")

root=tk.Tk()
r_label=tk.Label(root,text="radius is:").pack()
r_entry=tk.Entry(root).pack()

h_label=tk.Label(root,text="height is:").pack()
h_entry=tk.Entry(root).pack()

button=tk.Button(root,text="calculate",command=cal).pack()
button=tk.Entry(root).pack()

surface=tk.Label(root,text="").pack()
volumee=tk.Label(root,text="").pack()

root.mainloop()