import tkinter as tk

def convert():
   temp= entry.get()
   if temp.strip()=="":
   result_label.config(text="Enter a value")
   return

   try:
        temp = float(temp)
        if var.get() == 1: 
            converted = (temp * 9/5) + 32
            result_label.config(text=f"{converted:.2f} F")
        else: 
            converted = (temp - 32) * 5/9
            result_label.config(text=f"{converted:.2f} C")
    except ValueError:
        result_label.config(text="Invalid Input!")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")






