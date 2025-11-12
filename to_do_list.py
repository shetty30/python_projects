import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():   
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour To-Do List:")
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['task']} {status}")
    print()

# Main CLI loop
def main():
    tasks = load_tasks()
    print("Welcome to CLI To-Do List!")
    print("Commands: add <task>, view, done <num>, delete <num>, exit")

    while True:
        command = input("\nEnter command: ").strip().split(" ", 1)
        action = command[0].lower()

        if action == "add":
            if len(command) < 2:
                print("Please enter a task.")
                continue
            task_text = command[1]
            tasks.append({"task": task_text, "done": False})
            save_tasks(tasks)
            print(f"Added: '{task_text}'")

        elif action == "view":
            view_tasks(tasks)

        elif action == "done":
            if len(command) < 2 or not command[1].isdigit():
                print("Usage: done <task number>")
                continue
            index = int(command[1]) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                save_tasks(tasks)
                print(f"Marked as done: {tasks[index]['task']}")
            else:
                print("Invalid task number.")

        elif action == "delete":
            if len(command) < 2 or not command[1].isdigit():
                print("Usage: delete <task number>")
                continue
            index = int(command[1]) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"Deleted: {removed['task']}")
            else:
                print("Invalid task number.")

        elif action == "exit":
            print("Goodbye 👋")
            break

        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()        

        