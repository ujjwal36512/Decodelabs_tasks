from task_engine import TaskEngine
from tabulate import tabulate

class ToDoApp:
    """Command-line interface for the To-Do List application"""
    
    def __init__(self):
        self.engine = TaskEngine()
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("         TO-DO LIST APPLICATION")
        print("="*50)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks")
        print("4. View Completed Tasks")
        print("5. Update Task")
        print("6. Mark Task Complete")
        print("7. Mark Task Pending")
        print("8. Delete Task")
        print("9. Task Statistics")
        print("0. Exit")
        print("="*50)
    
    def add_task(self):
        """INPUT: Add a new task"""
        title = input("Enter task title: ").strip()
        if not title:
            print("❌ Title cannot be empty!")
            return
        
        description = input("Enter task description (optional): ").strip()
        task = self.engine.add_task(title, description)
        print(f"✅ Task added successfully! (ID: {task['id']})")
    
    def display_tasks(self, tasks, title="Tasks"):
        """OUTPUT: Display tasks in table format"""
        if not tasks:
            print(f"\n📭 No {title.lower()} found!")
            return
        
        table_data = []
        for task in tasks:
            table_data.append([
                task['id'],
                task['title'],
                task['description'][:30] + "..." if len(task['description']) > 30 else task['description'],
                task['status'],
                task['created_at'][:10]
            ])
        
        headers = ["ID", "Title", "Description", "Status", "Created"]
        print(f"\n{title}:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    def view_all_tasks(self):
        """OUTPUT: View all tasks"""
        tasks = self.engine.view_all_tasks()
        self.display_tasks(tasks, "All Tasks")
    
    def view_pending_tasks(self):
        """OUTPUT: View pending tasks"""
        tasks = self.engine.view_pending_tasks()
        self.display_tasks(tasks, "Pending Tasks")
    
    def view_completed_tasks(self):
        """OUTPUT: View completed tasks"""
        tasks = self.engine.view_completed_tasks()
        self.display_tasks(tasks, "Completed Tasks")
    
    def update_task(self):
        """PROCESS: Update a task"""
        self.view_all_tasks()
        try:
            task_id = int(input("\nEnter task ID to update: "))
        except ValueError:
            print("❌ Invalid ID!")
            return
        
        task = self.engine.view_task(task_id)
        if not task:
            print("❌ Task not found!")
            return
        
        print(f"\nCurrent task: {task['title']}")
        title = input("Enter new title (leave empty to skip): ").strip()
        description = input("Enter new description (leave empty to skip): ").strip()
        
        updated_task = self.engine.update_task(
            task_id,
            title=title if title else None,
            description=description if description else None
        )
        print(f"✅ Task updated successfully!")
    
    def mark_complete(self):
        """PROCESS: Mark task as complete"""
        self.view_pending_tasks()
        try:
            task_id = int(input("\nEnter task ID to mark complete: "))
        except ValueError:
            print("❌ Invalid ID!")
            return
        
        if self.engine.mark_complete(task_id):
            print("✅ Task marked as completed!")
        else:
            print("❌ Task not found!")
    
    def mark_pending(self):
        """PROCESS: Mark task as pending"""
        self.view_completed_tasks()
        try:
            task_id = int(input("\nEnter task ID to mark pending: "))
        except ValueError:
            print("❌ Invalid ID!")
            return
        
        if self.engine.mark_pending(task_id):
            print("✅ Task marked as pending!")
        else:
            print("❌ Task not found!")
    
    def delete_task(self):
        """PROCESS: Delete a task"""
        self.view_all_tasks()
        try:
            task_id = int(input("\nEnter task ID to delete: "))
        except ValueError:
            print("❌ Invalid ID!")
            return
        
        task = self.engine.view_task(task_id)
        if task:
            confirm = input(f"Delete '{task['title']}'? (y/n): ").lower()
            if confirm == 'y':
                if self.engine.delete_task(task_id):
                    print("✅ Task deleted successfully!")
            else:
                print("❌ Deletion cancelled!")
        else:
            print("❌ Task not found!")
    
    def show_statistics(self):
        """OUTPUT: Display task statistics"""
        total = self.engine.get_task_count()
        completed = self.engine.get_completed_count()
        pending = total - completed
        
        print("\n" + "="*50)
        print("         TASK STATISTICS")
        print("="*50)
        print(f"📊 Total Tasks: {total}")
        print(f"✅ Completed: {completed}")
        print(f"⏳ Pending: {pending}")
        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"📈 Completion Rate: {completion_rate:.1f}%")
        print("="*50)
    
    def run(self):
        """Main application loop"""
        print("\n🎉 Welcome to DecodeLabs To-Do List Application!")
        print("Following the IPO Model: Input → Process → Output")
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (0-9): ").strip()
            
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_all_tasks()
            elif choice == '3':
                self.view_pending_tasks()
            elif choice == '4':
                self.view_completed_tasks()
            elif choice == '5':
                self.update_task()
            elif choice == '6':
                self.mark_complete()
            elif choice == '7':
                self.mark_pending()
            elif choice == '8':
                self.delete_task()
            elif choice == '9':
                self.show_statistics()
            elif choice == '0':
                print("\n👋 Thank you for using To-Do List App!")
                print("Your tasks have been saved to tasks.json")
                break
            else:
                print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    app = ToDoApp()
    app.run()
