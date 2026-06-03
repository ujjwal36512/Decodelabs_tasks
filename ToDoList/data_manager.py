import json
import os
from datetime import datetime

class DataManager:
    """
    Handles persistence layer - moving data from volatile Memory (RAM) to permanent Storage.
    Converts between Python data structures and JSON file format.
    """
    
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.ensure_file_exists()
    
    def ensure_file_exists(self):
        """Create tasks.json if it doesn't exist"""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f, indent=2)
    
    def load_tasks(self):
        """Load all tasks from JSON file (Read from Storage to Memory)"""
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def save_tasks(self, tasks):
        """Save all tasks to JSON file (Write from Memory to Storage)"""
        with open(self.filename, 'w') as f:
            json.dump(tasks, f, indent=2)
    
    def get_next_id(self, tasks):
        """Generate next available ID (Dictionary 'id' -> Primary Key concept)"""
        if not tasks:
            return 1
        return max(task['id'] for task in tasks) + 1
