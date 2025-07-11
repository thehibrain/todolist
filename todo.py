# todo.py

import json
import os

DATA_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("[!] Corrupted task file. Starting fresh.")
        return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("\n[No tasks yet!]")
        return

    print("\n=== To-Do List ===")
    for idx, task in enumerate(tasks):
        status = "✔️" if task["done"] else "❌"
        print(f"{idx + 1}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Task name: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("[+] Task added.\n")

def mark_complete(tasks):
    list_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= choice < len(tasks):
            tasks[choice]["done"] = True
            save_tasks(tasks)
            print("[✓] Task marked complete.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: ")) - 1
        if 0 <= choice < len(tasks):
            removed = tasks.pop(choice)
            save_tasks(tasks)
            print(f"[–] Deleted: {removed['title']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n=== ToDo CLI ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("> ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
