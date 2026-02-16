# 🧾 Task Reminder CLI App
# 🎯 Purpose: Add, view, delete, and mark tasks as completed — all via command line
# 🧠 Concepts Used: Classes, Lists, Dictionaries, Loops, Conditionals, Input Handling

# --------------------------
# 📦 Task Class (Data Holder)
# --------------------------
class Task:
    def __init__(self, name, deadline, status):
        # Each Task instance stores its details in a dictionary
        self.task = {}
        self.name = name
        self.deadline = deadline
        self.status = status
        # Store data neatly in a dict
        self.task['Name'] = self.name
        self.task['Deadline'] = self.deadline
        self.task['Status'] = self.status


# --------------------------------
# 🧠 TaskReminder Class (Main App)
# --------------------------------
class TaskReminder:
    # Shared list for storing all task dictionaries
    tasks = []

    # 🧾 Show Main Menu
    def show_menu(self):
        print("\n" + "="*40)
        print("📅        TASK REMINDER APP")
        print("="*40)
        print("1️⃣  Add Task")
        print("2️⃣  View All Tasks")
        print("3️⃣  Delete Task")
        print("4️⃣  Mark Task as Completed")
        print("5️⃣  Exit")
        print("="*40)

    # ➕ Add a New Task
    def add_task(self):
        print("\n📝 Add a New Task")
        print("-"*30)
        name = input("Enter Name of the Task: ").strip()
        deadline = input("Enter Deadline (e.g., 30-10-2025): ").strip()
        status = input("Enter Status (e.g., Pending/In Progress): ").strip()

        # Create and append new task
        new_task = Task(name, deadline, status)
        self.tasks.append(new_task.task)

        print(f"\n✅ Task '{name}' added successfully!")

    # 👀 View All Tasks
    def view_tasks(self):
        if not self.tasks:
            print("\n📭 No tasks yet. Add one to get started!")
            return
        print("\n📋 Your Tasks:")
        print("-"*60)
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. 🧩 Name: {task['Name']}\n   ⏰ Deadline: {task['Deadline']}\n   📌 Status: {task['Status']}")
            print("-"*60)

    # ❌ Delete a Task by Name
    def delete_task(self):
        if not self.tasks:
            print("\n📭 No tasks yet.")
            return

        name = input("Enter Name of the Task to Delete: ").strip()
        found = False

        for task in self.tasks:
            if task['Name'].casefold() == name.casefold():
                self.tasks.remove(task)
                found = True
                print(f"\n🗑️  Task '{name}' deleted successfully!")
                break

        if not found:
            print("\n⚠️  Task not found!")

    # ✅ Mark a Task as Completed
    def mark_as_complete(self):
        if not self.tasks:
            print("\n📭 No tasks yet.")
            return

        name = input("Enter Name of the Task to Mark as Done: ").strip()
        found = False

        for task in self.tasks:
            if task['Name'].casefold() == name.casefold():
                task['Status'] = "✅ Done"
                found = True
                print(f"\n🎉 Task '{name}' marked as completed!")
                break

        if not found:
            print("\n⚠️  Task not found!")


# --------------------------
# 🚀 Main Application Loop
# --------------------------
if __name__ == "__main__":
    first_list = TaskReminder()

    while True:
        first_list.show_menu()

        # 🧭 Get user choice safely
        try:
            choice = int(input("👉 Choose one of the above options (1–5): "))
            if choice < 1 or choice > 5:
                print("⚠️  Please select a valid option (1–5).")
                continue
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        # 🎬 Execute user choice
        if choice == 1:
            first_list.add_task()
        elif choice == 2:
            first_list.view_tasks()
        elif choice == 3:
            first_list.delete_task()
        elif choice == 4:
            first_list.mark_as_complete()
        elif choice == 5:
            print("\n👋 Exiting Task Reminder App. Have a productive day!")
            break

        input("\n🔁 Press Enter to return to menu...")
