import tkinter as tk
from tkinter import ttk

# Task class
class Task:
    def __init__(self, name, description, due_date, priority):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Complete" if self.completed else "Incomplete"
        return f"{self.name} - {status}\n  Description: {self.description}\n  Due: {self.due_date}\n  Priority: {self.priority}"

# GUI class
class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        #Styling
        style = ttk.Style()

        style.configure("TFrame", background="#333")
        style.configure("TButton", background="#333", foreground="#ccc", font=("Arial", 10))
        
        # Main frame to hold everything
        self.main_frame = ttk.Frame(root, padding=10)
        self.main_frame.grid(sticky="NSEW")

        # Task list to hold all tasks
        self.tasks = []

        # Labels and Entry widgets
        tk.Label(self.main_frame, text='Task Name').grid(column=0, row=0, padx=5, pady=5, sticky="E")
        tk.Label(self.main_frame, text='Description').grid(column=0, row=1, padx=5, pady=5, sticky="E")
        tk.Label(self.main_frame, text='Due Date').grid(column=0, row=2, padx=5, pady=5, sticky="E")
        tk.Label(self.main_frame, text='Priority').grid(column=0, row=3, padx=5, pady=5, sticky="E")

        self.e1 = tk.Entry(self.main_frame, width=30)
        self.e2 = tk.Entry(self.main_frame, width=30)
        self.e3 = tk.Entry(self.main_frame, width=30)
        self.e4 = tk.Entry(self.main_frame, width=30)
        self.e1.grid(row=0, column=1, padx=5, pady=5, sticky="W")
        self.e2.grid(row=1, column=1, padx=5, pady=5, sticky="W")
        self.e3.grid(row=2, column=1, padx=5, pady=5, sticky="W")
        self.e4.grid(row=3, column=1, padx=5, pady=5, sticky="W")

        # Buttons
        self.button_frame = ttk.Frame(self.main_frame, padding=5)
        self.button_frame.grid(column=0, row=4, columnspan=2, pady=10)

        tk.Button(self.button_frame, text="Add Task", command=self.add_task).grid(column=0, row=0, padx=5)
        tk.Button(self.button_frame, text="Edit Task", command=self.edit_task).grid(column=1, row=0, padx=5)
        tk.Button(self.button_frame, text="Mark Complete", command=self.mark_complete).grid(column=2, row=0, padx=5)
        tk.Button(self.button_frame, text="Quit", command=root.quit).grid(column=3, row=0, padx=5)

        # Displaying tasks in a Text widget
        self.task_display = tk.Text(self.main_frame, height=10, width=50)
        self.task_display.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def add_task(self):
        name = self.e1.get()
        description = self.e2.get()
        due_date = self.e3.get()
        priority = self.e4.get()

        if name and description and due_date and priority:
            task = Task(name, description, due_date, priority)
            self.tasks.append(task)
            self.update_task_display()
            print(f"Task '{name}' added.")
            self.e1.delete(0, tk.END)
            self.e2.delete(0, tk.END)
            self.e3.delete(0, tk.END)
            self.e4.delete(0, tk.END)
        else:
            print("Please fill in all fields.")

    def mark_complete(self):
        task_name = self.e1.get()
        if task_name:
            task_found = False
            for task in self.tasks:
                if task.name == task_name:
                    task.mark_complete()
                    task_found = True
                    print(f"Task '{task_name}' marked as complete.")
                    self.update_task_display()
                    break
            if not task_found:
                print(f"Task '{task_name}' not found.")
        else:
            print("Please enter the task name to mark complete.")

    def update_task_display(self):
        # Clear the text widget and update with current tasks
        self.task_display.delete(1.0, tk.END)
        for task in self.tasks:
            self.task_display.insert(tk.END, str(task) + "\n")

    def edit_task(self):
        task_name = self.e1.get()
        if task_name:
            task_found = False
            for task in self.tasks:
                if task.name == task_name:
                    task_found = True
                    print(f"Task '{task_name}' found.")
                    task.name = self.e1.get()
                    task.description = self.e2.get()
                    task.due_date = self.e3.get()
                    task.priority = self.e4.get()
                    print(f"Task '{task_name}' edited.")
                    self.update_task_display()
            if not task_found:
                print(f"Task '{task_name}' not found.")
        else:
            print("Please enter the task name to edit.")
        
if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()