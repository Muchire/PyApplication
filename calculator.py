from tkinter import *

import tkinter as tk
#
# def on_button_click(value):
#     current = entry.get()
#     entry.delete(0,tk.END)
#     entry.insert(tk. END,current + value)
# def calculate():
#     try:
#         result=eval(entry.get())
#         entry.delete(0,tk.END)
#         entry.insert(tk.END,str(result))
#     except Exception as e:
#         entry.delete(0,tk.END)
#
# def clear_entry():
#     entry.delete(0,tk.END)
#
import tkinter as tk

# Function to update the display with button clicks
def button_click(item):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + item)

# Function to clear the display
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression and display the result
def button_equal():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, result)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry field
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Create Clear button
clear_button = tk.Button(root, text="Clear", padx=30, pady=10, command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Create Equal button
equal_button = tk.Button(root, text="=", padx=82, pady=10, command=button_equal)
equal_button.grid(row=5, column=2, columnspan=2)

# Run the main event loop
root.mainloop()