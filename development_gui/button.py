import tkinter as tk
def on_button_click():
    label.config(text="Button Clicked!")

root= tk.Tk()
root.title("Button Example")
root.geometry("300x200")

frame_top=tk.Frame(root)
frame_top.pack(side=tk.TOP, pady=10)

frame_bottom=tk.Frame(root)
frame_bottom.pack(side=tk.BOTTOM, pady=10)

label = tk.Label(root, text="Click the button", bg="lightblue")
label.pack(pady=20)

button = tk.Button(root, text="Click Me",command=on_button_click, bg="lightgreen")
button.pack(pady=20)

root.mainloop()
