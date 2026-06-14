import tkinter as tk
from main import *

# -----------------------------
# Root Window
# -----------------------------
root = tk.Tk()
root.geometry("400x500")
root.title("TO-Do List")
root.config(bg="#f0f4f8")

# -----------------------------
# Functions (GUI Logic)
# -----------------------------

def refresh_listbox():
    listbox.delete(0, tk.END)

    for task in view_tasks():
        status = "✅" if task["completed"] else "❌"
        display = f"{task['task_id']} | {task['task']} | {status}"
        listbox.insert(tk.END, display)


def handle_add():
    task_text = task_entry.get().strip()
    
    if add_task(task_text):
        task_entry.delete(0, tk.END)
        refresh_listbox()


def get_selected_task_id():
    selected = listbox.curselection()
    
    if not selected:
        return None
    
    index = selected[0]
    task = view_tasks()[index]
    return task["task_id"]


def handle_complete():
    task_id = get_selected_task_id()
    
    if task_id is not None:
        mark_complete(task_id)
        refresh_listbox()


def handle_delete():
    task_id = get_selected_task_id()
    
    if task_id is not None:
        delete_task(task_id)
        refresh_listbox()


# -----------------------------
# Header Frame
# -----------------------------
header_frame = tk.Frame(root, bg="lightblue", pady=10)
header_frame.pack(fill='x')

header_title = tk.Label(
    header_frame,
    text="To-Do App",
    font=("Times New Roman", 22, "bold"),
    bg="lightblue",
    fg="#003366"
)
header_title.pack()

# -----------------------------
# Input Frame
# -----------------------------
top_frame = tk.Frame(root, bg="#f0f4f8", pady=10)
top_frame.pack(fill="x", padx=10)

task_entry = tk.Entry(top_frame, font=('Arial', 16), bd=2, relief="solid")
task_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))
top_frame.grid_columnconfigure(0, weight=1)

add_btn = tk.Button(
    top_frame,
    text="Add Task",
    bg="#90ee90",
    font=("Arial", 12, "bold"),
    width=12,
    command=handle_add
)
add_btn.grid(row=0, column=1, padx=(5, 0))

# Enter key support
task_entry.bind("<Return>", lambda event: handle_add())

# -----------------------------
# Middle Frame (Listbox)
# -----------------------------
mid_frame = tk.Frame(root, bg="#f0f4f8", pady=5)
mid_frame.pack(fill='both', expand=True, padx=10)

listbox = tk.Listbox(
    mid_frame,
    font=("Arial", 14),
    bg="#ffffff",
    fg="#000000",
    selectbackground="#cce5ff"
)
listbox.grid(row=0, column=0, sticky='nsew')

scrollbar = tk.Scrollbar(mid_frame, orient="vertical")
scrollbar.grid(row=0, column=1, sticky="ns")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

mid_frame.grid_rowconfigure(0, weight=1)
mid_frame.grid_columnconfigure(0, weight=1)

# -----------------------------
# Bottom Frame (Buttons)
# -----------------------------
bottom_frame = tk.Frame(root, bg="#f0f4f8", pady=10)
bottom_frame.pack(fill='x', padx=10)

bottom_frame.grid_columnconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(1, weight=1)

complete_btn = tk.Button(
    bottom_frame,
    text="Complete Task",
    font=('Arial', 14, 'bold'),
    bg="#add8e6",
    fg="#003366",
    command=handle_complete
)
complete_btn.grid(row=0, column=0, sticky="ew", padx=(0, 5))

delete_btn = tk.Button(
    bottom_frame,
    text="Delete Task",
    font=('Arial', 14, 'bold'),
    bg="#ff9999",
    fg="#660000",
    command=handle_delete
)
delete_btn.grid(row=0, column=1, sticky="ew", padx=(5, 0))

# -----------------------------
# Initial Load
# -----------------------------
refresh_listbox()

# -----------------------------
# Run App
# -----------------------------
root.mainloop()