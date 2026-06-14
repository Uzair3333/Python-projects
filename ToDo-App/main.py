import json

error = ''
next_id = 1
tasks = []
try:
    with open('tasks.json', 'r') as f:
        f.seek(0)
        tasks = json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError) as fer:
    error = fer
for task in tasks:
    if task['task_id']>=next_id:
        next_id = task["task_id"] + 1

def save_tasks():
    try:
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=4)
        return True
    except TypeError as e:
        error = e
        return False

# Add a new task
def add_task(task_name):
    global next_id
    if task_name:
        tasks.append(
            {
                "task_id": next_id,
                "task": task_name,
                "completed": False
                })
        next_id += 1
        save_tasks()
        return True
    return False
    

# View all tasks with formatted output
def view_tasks():
    return tasks

# Mark a task as complete
def mark_complete( id_tsk_to_mrk):
    for task in tasks:
        if task["task_id"] == id_tsk_to_mrk:
            task["completed"] = True
            save_tasks()
            return True
    return False

# Delete a task by name
def delete_task( tsk_id):
    for task in tasks:
        if task["task_id"] == tsk_id:
            tasks.remove(task)
            save_tasks()
            return True
    return False
