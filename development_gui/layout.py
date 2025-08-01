import tkinter as tk 
root= tk.Tk()
root.title("combine layout")

frame_top=tk.Frame(root)
frame_bottom=tk.Frame(root)

frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

label1=tk.Label(frame_top, text=" top frame label 1", bg="orange")
label2=tk.Label(frame_top, text=" top frame label 2", bg="pink")
label3=tk.Label(frame_bottom, text=" bottom frame label 3", bg="yellow")
label4=tk.Label(frame_bottom, text=" bottom framelabel 4", bg="blue")

label1.pack(side=tk.LEFT)
label2.pack(side=tk.RIGHT)
label3.grid(row=0, column=0)
label4.grid(row=1, column=1)


root.geometry("400x300")
root.mainloop()