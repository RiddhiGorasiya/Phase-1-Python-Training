todo_list = []

def add_task():
    task = input("Enter a task: ")
    todo_list.append({"Task": task})
    print("New task added successfuly\n")

def view_task():
    print("Your TO-DO list: ")
    if len(todo_list) == 0:
        print("No pending taska!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']}")
    print("\n")

def remove_task():
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove: ")) -1
            if 0 <= search_index < len(todo_list):
                remove_task = todo_list.pop(search_index)
                print(f"task removed: {remove_task}")
            else:
                print("Invalis task number: ")
        except ValueError:
            print("Please enter a valid number.")


def menu():
    while (True):
        print("*** Main Menu ***")
        print("1. Add a new task")
        print("2. View all task")
        print("3. remove a task")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()        
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the appliction...")
            exit()
        else:
            print("Invalid choice! Try again!!")

menu()