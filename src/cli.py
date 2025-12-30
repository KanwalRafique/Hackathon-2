import sys
from .manager import TodoManager

def print_menu():
    print("\n--- 📝 Todo App Menu ---")
    print("1. ➕ Add Task")
    print("2. 👀 View All Tasks")
    print("3. ✏️ Update Task")
    print("4. 🗑 Delete Task")
    print("5. ✔️ Mark Complete / 🔄 Incomplete")
    print("6. 🚪 Exit")

def run_cli():
    manager = TodoManager()

    while True:
        print_menu()
        choice = input("\n👉 Enter choice (1-6): ")

        if choice == '1':
            title = input("Title: ")
            desc = input("Description: ")
            task = manager.add_task(title, desc)
            print(f"📝 Task added successfully! ID: {task.id}")

        elif choice == '2':
            tasks = manager.get_all_tasks()
            if not tasks:
                print("📭 No tasks found.")
            else:
                print("\nID | Status | Title")
                print("-" * 25)
                for t in tasks:
                    status = "✅" if t.is_completed else "⏳"
                    print(f"{t.id:<2} | {status:<6} | {t.title}")

        elif choice == '3':
            try:
                task_id = int(input("Task ID to update: "))
                title = input("New Title (leave blank to keep): ")
                desc = input("New Description (leave blank to keep): ")

                success = manager.update_task(
                    task_id,
                    title=title if title else None,
                    description=desc if desc else None
                )
                if success:
                    print("🔄 Task updated successfully!")
                else:
                    print("⚠️ Task not found.")
            except ValueError:
                print("❌ Invalid ID format.")

        elif choice == '4':
            try:
                task_id = int(input("Task ID to delete: "))
                if manager.delete_task(task_id):
                    print("❌ Task deleted successfully.")
                else:
                    print("⚠️ Task not found.")
            except ValueError:
                print("❌ Invalid ID format.")

        elif choice == '5':
            try:
                task_id = int(input("Task ID to toggle: "))
                new_status = manager.toggle_completion(task_id)
                if new_status is not None:
                    status_str = "Completed ✅" if new_status else "Incomplete ⏳"
                    print(f"✨ Task marked as {status_str}.")
                else:
                    print("⚠️ Task not found.")
            except ValueError:
                print("❌ Invalid ID format.")

        elif choice == '6':
            print("👋 Goodbye!")
            sys.exit()

        else:
            print("🚫 Invalid choice. Try again.")
