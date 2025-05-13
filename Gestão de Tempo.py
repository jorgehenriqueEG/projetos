import datetime

def add_task(tasks):
    task_name = input("Enter the task name: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
        tasks.append({"name": task_name, "due_date": due_date})
        print("Task added successfully!")
    except ValueError:
        print("Invalid date format. Please try again.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']} - Due: {task['due_date']}")

def main():
    tasks = []
    while True:
        print("\nTime Management Tool")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()