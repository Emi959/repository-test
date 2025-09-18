5# Minimal To-Do List App with Correct "TEST" ASCII Art

tasks = []

def print_ascii_title():
    print(r"""
  _______ ______  _____ _______
 |__   __|  ____|/ ____|__   __|
    | |  | |__  | (___    | |
    | |  |  __|  \___ \   | |
    | |  | |____ ____) |  | |
    |_|  |______|_____/   |_|

    """)
    print(">> Terminal Task Manager - TEST MODE <<\n")

def show_menu():
    print("======= MENU =======")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    print("====================")

def view_tasks():
    if not tasks:
        print("\n🗒️  No tasks yet!")
    else:
        print("\n📝 Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("✅ Task added!")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"❌ Removed task: {removed}")
        else:
            print("⚠️  Invalid number!")
    except ValueError:
        print("⚠️  Please enter a number.")

def main():
    print_ascii_title()
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("\n[Session Ended] Stay sharp. 🧠")
            break
        else:
            print("⚠️  Invalid choice. Try again.")

if __name__ == "__main__":
    main()
