import tkinter as tk
def mul():
    try:
        num=int(entry.get())
      #  output.delete('1.0',tk.END)
        for i  in range(1,11):
            output.insert(tk.END,f"{num}x{i}={num*i}\n")
    except :
        #output.delete('1.0',tk.END)
        output.insert(tk.END,"Invalid number!!")
root=tk.Tk()
root.title("multiplication Table")
label=tk.Label(root,text="enter the number")
label.pack()
entry=tk.Entry(root)
entry.pack()
button=tk.Button(root,text="answer",command=mul)
button.pack()
output=tk.Text(root)
output.pack()
root.mainloop()   