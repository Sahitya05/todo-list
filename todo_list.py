import tkinter as tk
from tkinter import messagebox, simpledialog

# Main Application
class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🗂️ To-Do List (Python Tkinter)")
        self.root.geometry("400x500")
        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self.root, text="My To-Do List", font=("Helvetica", 18, "bold"))
        self.title.pack(pady=10)

        # Entry + Add Button
        frame = tk.Frame(self.root)
        frame.pack()

        self.task_entry = tk.Entry(frame, width=25, font=("Arial", 14))
        self.task_entry.pack(side=tk.LEFT, padx=(10, 5))

        self.add_btn = tk.Button(frame, text="Add", width=8, command=self.add_task)
        self.add_btn.pack(side=tk.LEFT)

        # Task List
        self.task_listbox = tk.Listbox(self.root, width=40, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=20)

        # Action Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        self.edit_btn = tk.Button(button_frame, text="Edit", width=10, command=self.edit_task)
        self.edit_btn.grid(row=0, column=0, padx=5)

        self.delete_btn = tk.Button(button_frame, text="Delete", width=10, command=self.delete_task)
        self.delete_btn.grid(row=0, column=1, padx=5)

        self.complete_btn = tk.Button(button_frame, text="Complete", width=10, command=self.mark_completed)
        self.complete_btn.grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def edit_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            old_task = self.tasks[index]
            new_task = simpledialog.askstring("Edit Task", "Update the task:", initialvalue=old_task)
            if new_task:
                self.tasks[index] = new_task
                self.update_listbox()
        except:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def mark_completed(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index]
            if not task.endswith(" ✅"):
                self.tasks[index] = task + " ✅"
                self.update_listbox()
        except:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
