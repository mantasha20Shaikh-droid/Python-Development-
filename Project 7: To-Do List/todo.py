import json
import os

FILE_NAME = "todo.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, task):
    tasks.append({
        "task": task,
        "done": False
    })

    save_tasks(tasks)
    print("Task added.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, item in enumerate(tasks, start=1):
        status = "Done" if item["done"] else "Pending"
        print(i, ".", item["task"], "-", status)


def complete_task(tasks, number):
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    tasks[number - 1]["done"] = True
    save_tasks(tasks)

    print("Task completed.")


def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add")
        print("2. List")
        print("3. Done")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            list_tasks(tasks)
            number = int(input("Enter task number: "))
            complete_task(tasks, number)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
