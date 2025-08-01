import tkinter as tk 

def on_scale_change(value):
    label_value.config(text=f"Value: {value}")

# Create application window
root = tk.Tk()
root.title("Scale Window")
root.geometry("200x300")

frame = tk.Frame(root)
frame.pack()  # Make sure frame is visible

scale = tk.Scale(frame, from_=9000000000, to=10000000000, length=1000,orient=tk.HORIZONTAL, command=on_scale_change)
scale.pack()

label_value = tk.Label(root, text="Value: 9301582602")
label_value.pack()

root.mainloop()
