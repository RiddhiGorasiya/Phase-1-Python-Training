tasks = []  # Store all tasks

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty.")

def update_task():
    show_tasks()
    if tasks:
        try:
            index = int(input("Enter the task number to update: "))
            if 1 <= index <= len(tasks):
                new_task = input("Enter the updated task: ").strip()
                if new_task:
                    old_task = tasks[index - 1]
                    tasks[index - 1] = new_task
                    print(f"Task '{old_task}' updated to '{new_task}' successfully!")
                else:
                    print("Updated task cannot be empty.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    show_tasks()
    if tasks:
        try:
            index = int(input("Enter the task number to delete: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Task '{removed}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def menu():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ".strip())

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the app
menu()