import tkinter as tk
from tkinter import PhotoImage

# Create main window
root = tk.Tk()
root.title("My First Gui Program using Tkinter")

icon=PhotoImage(file="image.png")
root.iconphoto(True,icon)

root.geometry("400x300")

# pack inline block
# label1=tk.Label(root, text="label 1", bg="orange")
# label1.pack(fill=tk.BOTH,expand=True)

# label2=tk.Label(root, text="label 2", bg="pink")
# label2.pack(fill=tk.BOTH,expand=True)


# grid 
# 'label3=tk.Label(root, text="label 3", bg="yellow")
# label3.grid(row=0, column=0)

# label4=tk.Label(root, text="label 4", bg="blue")
# label4.grid(row=1, column=1')


# place 
label5=tk.Label(root, text="label 1", bg="pink")
label5.place(x=50, y=60)

label6=tk.Label(root, text="label 1", bg="green")
label6.place(x=100, y=200)
# Run the app
root.mainloop() # this is a function 

