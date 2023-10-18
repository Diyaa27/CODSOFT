# To-Do List Application

tasks = []

def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    status = "Incomplete"
    tasks.append({"title": title, "description": description, "status": status})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"Task {i}:")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print()

def update_task():
    title = input("Enter the title of the task to update: ")
    for task in tasks:
        if task["title"] == title:
            new_status = input("Enter the new status (e.g., Complete or Incomplete): ")
            task["status"] = new_status
            print("Task updated successfully!")
            return
    print("Task not found.")

def delete_task():
    title = input("Enter the title of the task to delete: ")
    for task in tasks:
        if task["title"] == title:
            tasks.remove(task)
            print("Task deleted successfully!")
            return
    print("Task not found.")

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
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
