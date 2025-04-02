from tkinter import *
# from tkinter.ttk import Combobox
# from tkinter.scrolledtext import ScrolledText

# Function to update the expression in the entry widget
def click_button(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + value)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Function to clear the entry widget
def clear():
    entry.delete(0, END)

# Function for backspace: remove the last character
def backspace():
    current = entry.get()
    entry.delete(len(current)-1, END)

# Create the main window
root = Tk()
root.title("Simple Calculator")
root.geometry("400x400")

# Entry widget to display the expression
entry = Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons for the calculator
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=5, height=2, font=('Arial', 18), command=evaluate).grid(row=row, column=col)
    else:
        Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda value=text: click_button(value)).grid(row=row, column=col)

# Add the backspace and clear button
Button(root, text="C", width=5, height=2, font=('Arial', 18), command=clear).grid(row=5, column=0, columnspan=2)
Button(root, text="Backspace", width=10, height=2, font=('Arial', 18), command=backspace).grid(row=5, column=2, columnspan=2)

# Start the Tkinter main loop
root.mainloop()
