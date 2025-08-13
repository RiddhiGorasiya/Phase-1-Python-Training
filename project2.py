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

# def delete_task(tasks, index):
#     if 1<= index <= len(tasks):
#         delete_task = tasks.pop(index-1)
#         print(f"Task '{delete_task}' deleted successfuly.")
#     else:
#         print("Invalid task index.")


def menu():
    while (True):
        print("*** Main Menu ***")
        print("1. Add a new task")
        print("2. View all task")
        print("3. Remove a task")
        # print("4. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()        
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        # elif choice == "4":
            # delete_task()
        elif choice == "4":
            print("Exiting the appliction...")
            exit()
        else:
            print("Invalid choice! Try again!!")

menu()


# def task():
#     tasks = []
#     print("*****Welcome to the to-do list*****")

#     total_task = int(input("Enter how manay task you want to add = "))
#     for i in range(1, total_task):
#         task_name = input(f"Enter task {i} = ")
#         tasks.append(task_name)

#     print(f"Today's tasks are\n{tasks}")

#     while True:
#         operation = int(input("Enter\n1-Add\n2-Updatr\n3-delete\n4-View\n5-Exit/stop/"))
#         if operation == 1:
#             add = input("Enter task you want to add = ")
#             tasks.append(add)
#             print(f"Task {add} has been successfully added...")
        
#         elif operation == 2:
#             updatrd_val = input("Enter task you want to update = ")
#             if updatrd_val in tasks:
#                 up = input("Enter new task = ")
#                 ind = tasks.index(updatrd_val)
#                 print(f"Updatrd task {up}")

# task()