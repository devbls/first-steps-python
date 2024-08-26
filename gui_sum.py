import tkinter as tk
from tkinter import messagebox

def sum_numbers():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 + num2
    messagebox.showinfo("Result", f"The sum is: {result}")

# Creating the window
window = tk.Tk()
window.title("Sum Calculator")

# Creating widgets
label_num1 = tk.Label(window, text = "Number 1:")
label_num1.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "e")

entry_num1 = tk.Entry(window)
entry_num1.grid(row = 0, column = 1, padx = 10, pady = 5)

label_num2 = tk.Label(window, text = "Number 2:")
label_num2.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = "e")

entry_num2 = tk.Entry(window)
entry_num2.grid(row = 1, column = 1, padx = 10, pady = 5)

sum_button = tk.Button(window, text = "Somar", command = sum_numbers)
sum_button.grid(row = 2, columnspan = 2, padx = 10, pady = 5)

window.mainloop()