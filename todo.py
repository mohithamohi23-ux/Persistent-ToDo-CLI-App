# todo.py
# Task 2 - Persistent Console To-Do Application

import os

FILE_NAME = "tasks.txt"

def load_tasks():
    """Load tasks from file into a list."""
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if "|" in line:
                    status, text = line.split("|", 1)
                    tasks.append([int(status), text])
    return tasks


def save_tasks(tasks):
    """Save all tasks back to the file."""
    with open(FILE_NAME, "w") as file:
        for status, text in tasks:
            file.write(f"{status}|{text}\n")


def view_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("No tasks available!")
        return

    print("\nYour Tasks:")
    for i, (status, text) in enumerate(tasks, start=1):
        symbol = "[x]" if status == 1 else "[ ]"
        print(f"{i}. {symbol} {text}")
    print()


def add_task(tasks, text):
    """Add a new task."""
    text = text.strip()
    if text == "":
        print("Cannot add an empty task.")
        return
    tasks.append([0, text])
    save_tasks(tasks)
    print(f"Added: {text}")


def remove_task(tasks, index):
    """Remove task by number."""
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed: {removed[1]}")
    except IndexError:
        print("Invalid task number.")


def mark_done(tasks, index):
    """Mark a task as completed."""
    try:
        tasks[index - 1][0] = 1
        save_tasks(tasks)
        print("Task marked as done.")
    except IndexError:
        print("Invalid task number.")


def clear_completed(tasks):
    """Remove all tasks that are marked done."""
    before = len(tasks)
    tasks[:] = [task for task in tasks if task[0] == 0]
    save_tasks(tasks)
    print(f"Cleared {before - len(tasks)} completed tasks.")


def print_menu():
    print("""
Commands:
 view               - Show all tasks
 add <task>         - Add a new task
 remove <number>    - Remove a task
 done <number>      - Mark task as done
 clear              - Delete completed tasks
 help               - Show commands
 exit               - Quit the app
""")


def main():
    tasks = load_tasks()
    print("Welcome to the Persistent To-Do Application!")
    print("Type 'help' to see all commands.\n")

    while True:
        cmd = input("> ").strip()

        if cmd == "":
            continue

        parts = cmd.split(" ", 1)
        action = parts[0]

        if action == "view":
            view_tasks(tasks)

        elif action == "add":
            if len(parts) == 1:
                text = input("Enter task: ")
            else:
                text = parts[1]
            add_task(tasks, text)

        elif action == "remove":
            if len(parts) == 1:
                print("Usage: remove <task_number>")
            else:
                try:
                    index = int(parts[1])
                    remove_task(tasks, index)
                except ValueError:
                    print("Please enter a valid number.")

        elif action == "done":
            if len(parts) == 1:
                print("Usage: done <task_number>")
            else:
                try:
                    index = int(parts[1])
                    mark_done(tasks, index)
                except ValueError:
                    print("Please enter a valid number.")

        elif action == "clear":
            clear_completed(tasks)

        elif action == "help":
            print_menu()

        elif action == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command. Type 'help'.")


if __name__ == "__main__":
    main()
