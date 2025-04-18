todo_list = []  

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task description: ")
    status = "Not Started" 
    todo_list.append({"task": task, "status": status})
    print("Task added successfully!")

def view_tasks():
    if not todo_list:
        print("No tasks available.")
    else:
        print("\n--- Your To-Do List ---")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item['task']} - [{item['status']}]")

def update_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to update: ")) - 1
        if 0 <= task_num < len(todo_list):
            # if (0 <= task_num) and (task_num < len(todo_list))
            new_task = input("Enter new task description: ")
            new_status = input("Enter new status (Not Started/In Progress/Completed): ")
            if new_status not in ["Not Started", "In Progress", "Completed"]:
                print("Invalid status. Keeping previous status.")
            else:
                todo_list[task_num]["status"] = new_status
            todo_list[task_num]["task"] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed_task = todo_list.pop(task_num)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
