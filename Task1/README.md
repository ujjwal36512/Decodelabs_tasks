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
