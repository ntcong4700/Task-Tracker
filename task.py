import os
import json
from tabulate import tabulate

FILE_PATH_HELP = "help_command.json"
FILE_PATH_DATA = "data.json"

def get_help_command():
    with open(FILE_PATH_HELP, "r") as file:
        data = json.load(file)
        return data

def load_data_tasks():
    tasks = []
    if os.path.exists(FILE_PATH_DATA) and os.path.getsize(FILE_PATH_DATA) > 0:
        with open(FILE_PATH_DATA, "r") as file:
            tasks = json.load(file)
    return tasks

def save_data_tasks(tasks):
    with open(FILE_PATH_DATA, "w") as file:
        json.dump(tasks, file)

def add_task(description):
    tasks = load_data_tasks()
    tasks_id = len(tasks) + 1
    task = {
        "id": tasks_id,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    save_data_tasks(tasks)
    print(f"Task with id {tasks_id} added successfully.")

def view_all_tasks():
    tasks = load_data_tasks()
    print(tabulate(tasks, headers="keys", tablefmt="fancy_grid"))

def update_task(task_id, new_description):
    tasks = load_data_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_data_tasks(tasks)
    print(f"Task with id {task_id} updated successfully.")

def delete_task(task_id):
    tasks = load_data_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task with id {task_id} deleted successfully.")

def mark_task_as_completed(task_id):
    tasks = load_data_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_data_tasks(tasks)
    print(f"Task with id {task_id} marked as completed successfully.")

if __name__ == "__main__":
    view_all_tasks()