#task.py
from tkinter import *
from tkinter import ttk
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
    
class GUI(Task):
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Frame Text Label").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
    root.mainloop()