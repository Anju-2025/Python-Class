import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("300x400")

        self.task_list = tk.Listbox(root, width=40, height=15)
        self.task_list.pack(pady=10)

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_tasks)
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        try:
            selected_task = self.task_list.curselection()[0]
            self.task_list.delete(selected_task)
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def clear_tasks(self):
        self.task_list.delete(0, tk.END)

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
