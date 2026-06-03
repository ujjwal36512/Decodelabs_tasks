from datetime import datetime
from data_manager import DataManager

class TaskEngine:
    """
    Core business logic engine following the IPO model:
    - Input: Task data entry
    - Process: Logic and modifications
    - Output: Display and results
    """
    
    def __init__(self, data_manager=None):
        self.data_manager = data_manager or DataManager()
        self.tasks = self.data_manager.load_tasks()
    
    # ============ INPUT PHASE ============
    def add_task(self, title, description=""):
        """
        Input: Create a new task dictionary.
        Dictionary structure: {'id': int, 'title': str, 'description': str, 'status': str, 'created_at': str}
        """
        task_id = self.data_manager.get_next_id(self.tasks)
        new_task = {
            'id': task_id,
            'title': title,
            'description': description,
            'status': 'pending',
            'created_at': datetime.now().isoformat()
        }
        self.tasks.append(new_task)  # list.append(row) -> INSERT INTO concept
        self.data_manager.save_tasks(self.tasks)
        return new_task
    
    # ============ PROCESS PHASE ============
    def update_task(self, task_id, title=None, description=None, status=None):
        """
        Process: Modify task properties.
        """
        task = self._find_task(task_id)
        if not task:
            return None
        
        if title is not None:
            task['title'] = title
        if description is not None:
            task['description'] = description
        if status is not None:
            task['status'] = status
        
        self.data_manager.save_tasks(self.tasks)
        return task
    
    def mark_complete(self, task_id):
        """Mark a task as completed"""
        return self.update_task(task_id, status='completed')
    
    def mark_pending(self, task_id):
        """Mark a task as pending"""
        return self.update_task(task_id, status='pending')
    
    def delete_task(self, task_id):
        """Remove a task from the collection"""
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.data_manager.save_tasks(self.tasks)
            return True
        return False
    
    # ============ OUTPUT PHASE ============
    def view_task(self, task_id):
        """Output: Display a specific task"""
        return self._find_task(task_id)
    
    def view_all_tasks(self):
        """Output: Display all tasks (List -> Full Database Table)"""
        return self.tasks
    
    def view_pending_tasks(self):
        """Output: Display only pending tasks"""
        return [task for task in self.tasks if task['status'] == 'pending']
    
    def view_completed_tasks(self):
        """Output: Display only completed tasks"""
        return [task for task in self.tasks if task['status'] == 'completed']
    
    # ============ HELPER METHODS ============
    def _find_task(self, task_id):
        """Find task by ID (Primary Key lookup)"""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def get_task_count(self):
        """Get total number of tasks"""
        return len(self.tasks)
    
    def get_completed_count(self):
        """Get count of completed tasks"""
        return len(self.view_completed_tasks())
