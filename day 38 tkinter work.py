from tkinter import *
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox  # Import messagebox for alerts

root = Tk()
root.title("Let us know how we can improve")
root.geometry("400x400")

a = StringVar()
b = StringVar()
c = StringVar()

# Function to validate and submit form
def submit_form():
    name = a.get().strip()
    email = b.get().strip()
    age = c.get().strip()
    role = combo.get().strip()
    rating = x.get()
    feedback = combo1.get().strip()
    comments = s1.get("1.0", END).strip()

    # Check for empty fields
    if not name or not email or not age or not role or not feedback or not comments or rating == 0:
        messagebox.showwarning("Input Error", "All fields are required!")
    else:
        messagebox.showinfo("Form Submission", "Thank you for your feedback!")

# Widgets
Label(root, text="Let us know how we can improve the service").grid(row=0, column=5)

Label(root, text="Name").grid(row=1, column=4)
Entry(root, textvariable=a).grid(row=1, column=5)

Label(root, text="Email").grid(row=2, column=4)
Entry(root, textvariable=b).grid(row=2, column=5)

Label(root, text="Age").grid(row=3, column=4)
Entry(root, textvariable=c).grid(row=3, column=5)

Label(root, text="Which option best describes your current role?").grid(row=4, column=4)
Label(root, text="How likely is it that you would recommend this to a friend").grid(row=5, column=4)
Label(root, text="What do you like most here?").grid(row=8, column=4)
Label(root, text="Things that should be improved in the future").grid(row=9, column=4)
Label(root, text="Any comments or suggestions?").grid(row=12, column=4)

# Comboboxes
combo = Combobox(root, values=("Student", "Professional", "Mentor"))
combo.current(0)
combo.grid(row=4, column=5)

combo1 = Combobox(root, values=("Teaching", "Practice", "Library"))
combo1.grid(row=8, column=5)

# Radio buttons for recommendation
x = IntVar()
Radiobutton(root, text="Definitely", variable=x, value=1).grid(row=5, column=5)
Radiobutton(root, text="Maybe", variable=x, value=2).grid(row=6, column=5)
Radiobutton(root, text="Not sure", variable=x, value=3).grid(row=7, column=5)

# Checkboxes (optional, so no validation needed)
Checkbutton(root, text="Front-end project").grid(row=9, column=5)
Checkbutton(root, text="Back-end project").grid(row=10, column=5)
Checkbutton(root, text="Data visualization").grid(row=11, column=5)

# Scrolled text for additional comments
s1 = ScrolledText(root, width=30, height=5)
s1.grid(row=12, column=5)

# Submit button with validation
Button(root, text="Submit", bg="blue", command=submit_form).grid(row=13, column=5)

root.mainloop()
