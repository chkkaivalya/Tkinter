import tkinter as tk
from tkinter import messagebox as mb
def add_task():
    task=task_enter.get()
    if task:
        listbox.insert(tk.END,task)
        task_enter.delete(0,tk.END)
    else:
        mb.showwarning(" Warning!! Task cannot be empty!")
def remove_task():
    try:
        selectTask=listbox.curselection()[0]
        listbox.delete(selectTask)
    except IndexError:
        mb.showwarning("No Task is Selected!!!!!")
def mark_done():
    try:
        selectTask=listbox.curselection()[0]
        task=listbox.get(selectTask)
        listbox.delete(selectTask)
        listbox.insert(0,f"✔ {task}")
    except IndexError:
        mb.showwarning("Please Select the Task to Mark it as Done!!")
def clear_all():
    listbox.delete(0,tk.End)

root=tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
task_enter=tk.Entry(root,width=40)
task_enter.pack(pady=10)
listbox=tk.Listbox(root,width=50,height=10)
listbox.pack(pady=10)
add_button=tk.Button(root,text="Add Your Task",command=add_task)
add_button.pack(pady=5)
remove_button=tk.Button(root,text="Remove the Task",command=remove_task)
remove_button.pack(pady=5)
clear_button=tk.Button(root,text="Clear All",command=clear_all)
clear_button.pack(pady=5)
done_button=tk.Button(root,text="Mark as Done",command=mark_done)
done_button.pack(pady=5)
root.mainloop()
