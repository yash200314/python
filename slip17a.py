import tkinter as tk

def convert_to_uppercase():
    text = input_field.get()
    text = text.upper()
    output_field.config(text=text)

# Create the main window
window = tk.Tk()

# Create the input field
input_field = tk.Entry(window)
input_field.pack()

# Create the button
convert_button = tk.Button(window, text="Convert to uppercase", command=convert_to_uppercase)
convert_button.pack()

# Create the output field
output_field = tk.Label(window)
output_field.pack()

# Start the main event loop
window.mainloop()
