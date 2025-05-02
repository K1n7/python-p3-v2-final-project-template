# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)

# lib/cli.py

from helpers import list_tasks, add_task, complete_task, delete_task, exit_program

def menu():
    print("\n--- Task Manager CLI ---")
    print("1. List all tasks")
    print("2. Add a new task")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
