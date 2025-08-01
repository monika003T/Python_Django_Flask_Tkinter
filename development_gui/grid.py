import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("My First Gui Program using Tkinter")

icon = PhotoImage(file="image.png")
root.iconphoto(True, icon)

# create different widgets
label = tk.Label(root, text="Click the button", bg="lightblue")
button = tk.Button(root, text="Click Me", bg="lightgreen")
entry = tk.Entry(root)
text = tk.Text(root, height=5, width=30)
checkbutton = tk.Checkbutton(root, text="Click me")
radiobutton1 = tk.Radiobutton(root, text="Option 1", value=1)
radiobutton2 = tk.Radiobutton(root, text="Option 2", value=2)

# Place widgets
label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
button.grid(row=0, column=1, padx=10, pady=10, sticky='e')
entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky='ew')
text.grid(row=2, column=2, columnspan=1, padx=10, pady=10, sticky='w')
checkbutton.grid(row=0, column=2, padx=10, pady=5, sticky='e')
radiobutton1.grid(row=2, column=2, padx=10, pady=10, sticky='w')
radiobutton2.grid(row=3, column=2, padx=10, pady=10, sticky='w')

root.geometry("400x300")
root.mainloop()
