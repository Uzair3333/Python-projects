# 🧾 Project: To-Do List CLI App (In-Memory Version)
# 🎯 Purpose: Manage daily tasks — add, view, complete, delete
# 🧠 Concepts: Classes, Lists, Loops, Conditionals, Functions, Input Handling

class ToDoList:
    def __init__(self):
        # Each ToDoList instance has its own list of tasks
        self.tasks = []

    # Display the main menu
    def show_menu(self):
        print("\n" + "="*35)
        print("🧾        TO-DO LIST MENU")
        print("="*35)
        print("1️⃣  Add Task")
        print("2️⃣  View Tasks")
        print("3️⃣  Mark Complete")
        print("4️⃣  Delete Task")
        print("5️⃣  Exit")
        print("="*35)

    # Add a new task
    def add_task(self):
        task_name = input("Enter new task: ").strip()
        if not task_name:
            print("⚠️  Task cannot be empty.")
            return
        self.tasks.append({"task": task_name, "completed": False})
        print(f"✅ Task '{task_name}' added successfully!")

    # View all tasks with formatted output
    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks yet! Add some to get started.")
            return
        print("\n🗂️  Your Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            status = "✅ Done" if task["completed"] else "❌ Not Done"
            print(f"  {i}. {task['task']} [{status}]")

    # Mark a task as complete
    def mark_complete(self):
        self.view_tasks()
        if not self.tasks:
            return
        task_to_complete = input("Enter the exact task name to mark complete: ").strip()
        for task in self.tasks:
            if task["task"].lower() == task_to_complete.lower():
                task["completed"] = True
                print(f"🎉 Task '{task_to_complete}' marked as complete!")
                break
        else:
            print("⚠️  Task not found!")

    # Delete a task by name
    def delete_task(self):
        self.view_tasks()
        if not self.tasks:
            return
        delete_name = input("Enter the exact task name to delete: ").strip()
        for task in self.tasks:
            if task["task"].lower() == delete_name.lower():
                self.tasks.remove(task)
                print(f"🗑️  Task '{delete_name}' deleted successfully!")
                break
        else:
            print("⚠️  Task not found!")

# --------------------------
# 🚀 Main App Loop
# --------------------------
first_list = ToDoList()

while True:
    first_list.show_menu()
    try:
        choice = int(input("👉 Choose one of the above options: "))
        if choice < 1 or choice > 5:
            print("⚠️  Please select a valid option (1–5).")
            continue
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        continue

    if choice == 1:
        first_list.add_task()
    elif choice == 2:
        first_list.view_tasks()
    elif choice == 3:
        first_list.mark_complete()
    elif choice == 4:
        first_list.delete_task()
    elif choice == 5:
        print("\n👋 Exiting To-Do List. Have a productive day!")
        break

    input("\n🔁 Press Enter to return to menu...")
