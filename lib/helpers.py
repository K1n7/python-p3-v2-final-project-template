# lib/helpers.py
# lib/helpers.py

from models.task import Task

def list_tasks():
    tasks = Task.all()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(task)

def add_task():
    description = input("Enter task description: ")
    Task(description)
    print("Task added.")

def complete_task():
    task_id = input("Enter task ID to mark complete: ")
    task = Task.get(int(task_id))
    if task:
        task.mark_complete()
        print("Task marked complete.")
    else:
        print("Task not found.")

def delete_task():
    task_id = input("Enter task ID to delete: ")
    task = Task.get(int(task_id))
    if task:
        Task.delete(task.id)
        print("Task deleted.")
    else:
        print("Task not found.")

def exit_program():
    print("Goodbye!")
    exit()

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
