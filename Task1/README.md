# To-Do List Application

A Python-based to-do list engine following the DecodeLabs IPO model (Input, Process, Output).

## Architecture

### IPO Model
- **Input (Data Entry)**: User commands and task creation
- **Process (Logic/Modification)**: Task management operations
- **Output (Display/View)**: Display tasks and results

### Data Structures
- **Task Dictionary**: Individual task with `id`, `title`, `description`, `status`, `created_at`
- **Task List**: Collection of task dictionaries (simulates database table)

## Data Persistence

Tasks are persisted to `tasks.json` file for permanent storage (moving from volatile memory to disk).

## Features

1. **Add Task**: Create new tasks with title and description
2. **View Tasks**: Display all tasks or specific task
3. **Update Task**: Modify task title, description, or status
4. **Delete Task**: Remove tasks from the list
5. **Mark Complete**: Change task status to completed
6. **List All**: Display all tasks in table format

## Usage

```bash
python main.py
```

## Project Structure

```
Task1/
├── main.py              # Main CLI application entry point
├── task_engine.py       # Core business logic (IPO Process layer)
├── data_manager.py      # Data persistence layer (Storage management)
├── README.md            # Project documentation
└── .gitignore           # Git ignore configuration
```

## Installation

1. Ensure Python 3.7+ is installed
2. Install required dependencies:
```bash
pip install tabulate
```

## Running the Application

```bash
python main.py
```

### Menu Options

1. **Add Task** - Create a new task with title and description
2. **View All Tasks** - Display all tasks in a formatted table
3. **View Pending Tasks** - Show only incomplete tasks
4. **View Completed Tasks** - Show only completed tasks
5. **Update Task** - Modify task title or description
6. **Mark Task Complete** - Change task status to completed
7. **Mark Task Pending** - Change task status back to pending
8. **Delete Task** - Remove a task from the list
9. **Task Statistics** - Display task summary and completion rate
0. **Exit** - Save and close the application

## Technical Implementation

### Layer 1: Input (main.py - ToDoApp class)
- Handles user interactions and menu display
- Validates input from users
- Calls appropriate engine methods

### Layer 2: Process (task_engine.py - TaskEngine class)
- Core business logic for task operations
- Manages task collection in memory
- Implements CRUD operations
- Interacts with data manager for persistence

### Layer 3: Output (main.py - Display methods)
- Formatted table display using tabulate
- User-friendly status messages
- Task statistics and metrics

### Layer 4: Storage (data_manager.py - DataManager class)
- JSON-based persistence
- File I/O operations
- Data validation and transformation

## Data Format

Tasks are stored as dictionaries with the following structure:

```python
{
    'id': 1,                              # Unique identifier (Primary Key)
    'title': 'Complete project',          # Task title
    'description': 'Finish the report',   # Task description
    'status': 'pending',                  # 'pending' or 'completed'
    'created_at': '2025-06-07T12:00:00'  # ISO format timestamp
}
```

## Time Complexity

- **Add Task**: O(1) - Constant time
- **View Tasks**: O(n) - Linear, where n is number of tasks
- **Update Task**: O(n) - Linear search then update
- **Delete Task**: O(n) - Linear search then removal
- **Mark Complete/Pending**: O(n) - Linear search then update

## Space Complexity

- Overall: O(n) - Proportional to number of tasks stored

## Future Enhancements

- [ ] Database integration (SQLite, PostgreSQL)
- [ ] User authentication
- [ ] Task categories/tags
- [ ] Due dates and reminders
- [ ] Task priority levels
- [ ] Search and filter functionality
- [ ] Data export (CSV, PDF)
- [ ] Web interface

## Author

DecodeLabs Internship Program

## License

MIT License
