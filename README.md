# DecodeLabs Internship - Tasks Repository

A comprehensive collection of Python-based projects demonstrating software engineering best practices, including architecture design, security implementation, and application development.

---

## 📚 Repository Contents

### 1. **To-Do List Application** (`ToDoList/`)
A Python-based task management system following the **IPO Model** (Input, Process, Output).

#### Features:
- ✅ **Add Task**: Create new tasks with title and description
- ✅ **View Tasks**: Display all tasks or specific task details
- ✅ **Update Task**: Modify task title, description, or status
- ✅ **Delete Task**: Remove tasks from the list
- ✅ **Mark Complete**: Change task status to completed
- ✅ **List All**: Display all tasks in table format

#### Architecture:
- **IPO Model Implementation**:
  - **Input (Data Entry)**: User commands and task creation
  - **Process (Logic/Modification)**: Task management operations
  - **Output (Display/View)**: Display tasks and results

#### Data Structures:
- **Task Dictionary**: Individual task with `id`, `title`, `description`, `status`, `created_at`
- **Task List**: Collection of task dictionaries (simulates database table)

#### Data Persistence:
- Tasks are persisted to `tasks.json` file for permanent storage

#### Usage:
```bash
cd ToDoList
python main.py
```

---

### 2. **Enterprise Password Generator** (`enterprise_password_generator.py`)
A production-grade password generator with enterprise-level security, implementing cryptographic best practices and mathematical security analysis.

#### Architecture Layers:

**Layer 1: Environment & Configuration**
- Configurable complexity levels: LOW, MEDIUM, HIGH, ENTERPRISE
- Environmental constraints and security policies
- Validation of configuration parameters

**Layer 2: Character Classification**
- Standardized character classification using Python's `string` module
- Ambiguous character handling (0/O, 1/l/I, etc.)
- Memory-efficient character set caching

**Layer 3: Cryptographic Security**
- `secrets.SystemRandom` for cryptographically secure randomness
- `os.urandom` for secure random byte generation
- Mathematical entropy calculation: **E = L × log₂(R)**
- NIST-based security ratings

**Layer 4: Memory Optimization**
- Accumulator pattern with list buffer
- Linear O(n) time complexity
- Efficient string joining
- Secure buffer clearing

**Layer 5: Enterprise Integration**
- Composable architecture
- Extensible design
- Production-ready error handling
- Comprehensive analysis metadata

**Layer 6: Analysis & Metrics**
- Information entropy calculation
- Security strength assessment
- Performance characterization
- Batch generation support

#### Preset Configurations:
- **LOW**: 8-12 chars, Uppercase + Lowercase
- **MEDIUM**: 12-16 chars, Uppercase + Lowercase + Digits
- **HIGH**: 16-24 chars, Uppercase + Lowercase + Digits + Special (no ambiguous)
- **ENTERPRISE**: 24-32 chars, Full Requirements (no ambiguous)

#### Security Analysis:
The generator calculates password entropy using the formula: **E = L × log₂(R)**

NIST Security Guidelines:
- < 28 bits: Weak ⚠️
- 28-60 bits: Fair ⚡
- 60-90 bits: Good ✓
- 90-128 bits: Strong ✓✓
- > 128 bits: Very Strong ✓✓✓

#### Performance:
- **Time Complexity**: O(n) - Linear with password length
- **Space Complexity**: O(n) - Linear for password storage
- **Batch Generation**: Efficiently generate multiple passwords

#### Usage:
```bash
python enterprise_password_generator.py
```

The script runs a comprehensive demonstration showing:
1. Low complexity password generation
2. Medium complexity password generation
3. High complexity password generation
4. Enterprise complexity password generation
5. Entropy analysis and security mathematics
6. Algorithm complexity analysis
7. Batch password generation
8. Architectural summary

---

### 3. **Advanced Expense Tracker** (`expence_tracker.py`)
A robust expense tracking application with kill switch functionality, graceful shutdown, and comprehensive error handling.

#### Key Features:
- ✅ **Multiple Transaction Handling**: Support for 5+ transactions
- ✅ **Kill Switch**: Sentinel value for program termination ("exit")
- ✅ **Graceful Shutdown**: Proper cleanup and state management
- ✅ **State Management**: Total initialized outside loop
- ✅ **Error Handling**: Comprehensive exception handling (ValueError, etc.)
- ✅ **Final Total Display**: Shows total on exit
- ✅ **Running Total**: Displays running total after each transaction
- ✅ **Summary View**: View expense summary at any time
- ✅ **Help System**: Built-in help and command documentation

#### Commands:
- `<amount>`: Add an expense (e.g., 100, 50.25)
- `EXIT`: Shutdown with kill switch (sentinel value)
- `SUMMARY`: View current expense summary
- `HELP`: Display help and available commands

#### Features Demonstration:
- Keyboard interrupt handling (Ctrl+C) with graceful shutdown
- EOF (End of File) handling
- Input validation with error messages
- Negative value rejection
- Zero value handling
- Non-numeric input handling

#### Usage:
```bash
python expence_tracker.py
```

Interactive example:
```
Enter expense amount (or 'EXIT' to exit): 100
✓ Added: $100.00 (Transaction #1)
  Running Total: $100.00

Enter expense amount (or 'EXIT' to exit): 50.25
✓ Added: $50.25 (Transaction #2)
  Running Total: $150.25

Enter expense amount (or 'EXIT' to exit): EXIT
```

---

## 📊 Technology Stack

- **Language**: Python 3.x
- **Standard Libraries**: 
  - `string`, `math`, `os`, `sys`
  - `secrets`, `dataclasses`, `enum`
  - `typing`
- **Architecture Patterns**: 
  - IPO Model (Input-Process-Output)
  - Layered Architecture
  - Object-Oriented Design
  - Accumulator Pattern

---

## 🎯 Learning Outcomes

This repository demonstrates:

1. **Software Architecture**: Multi-layered design patterns and separation of concerns
2. **Security**: Enterprise-grade password generation with cryptographic best practices
3. **State Management**: Proper initialization and management of program state
4. **Error Handling**: Comprehensive exception handling and validation
5. **Code Organization**: Clean code structure and documentation
6. **Performance Optimization**: Time and space complexity analysis
7. **User Experience**: Graceful error messages and helpful prompts
8. **Data Persistence**: JSON-based storage for permanent data retention
9. **Testing & Validation**: Input validation and security analysis

---

## 📝 File Structure

```
Decodelabs_tasks/
├── README.md                              # This file
├── ToDoList/
│   ├── README.md                          # To-Do List documentation
│   ├── main.py                            # Main application entry point
│   └── tasks.json                         # Persistent task storage
├── enterprise_password_generator.py       # Password generation system
└── expence_tracker.py                     # Expense tracking system
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher

### Installation
```bash
git clone https://github.com/ujjwal36512/Decodelabs_tasks.git
cd Decodelabs_tasks
```

### Running Projects

**To-Do List Application:**
```bash
cd ToDoList
python main.py
```

**Enterprise Password Generator:**
```bash
python enterprise_password_generator.py
```

**Expense Tracker:**
```bash
python expence_tracker.py
```

---

## 📖 Code Quality

- ✅ Type hints for better code clarity
- ✅ Comprehensive docstrings
- ✅ Error handling and validation
- ✅ Security best practices
- ✅ Performance optimization
- ✅ Clean code principles

---

## 💡 Key Concepts Implemented

### DecodeLabs IPO Model
- **Input**: User data collection and validation
- **Process**: Business logic and data manipulation
- **Output**: Formatted results and feedback

### Security & Cryptography
- Cryptographically secure random generation
- Entropy calculation and security analysis
- Password complexity requirements
- Safe character set management

### Design Patterns
- Class-based architecture
- Decorator pattern (for method chaining)
- Dataclass for configuration
- Enum for complexity levels

### State Management
- Proper initialization of variables
- State preservation during exceptions
- Graceful shutdown handling
- Running state tracking

---

## 📄 License

This repository is part of the DecodeLabs Internship program.

---

## 👨‍💻 Author

**Ujjwal Sharma** - DecodeLabs Intern

---

## 📞 Support

For questions or issues, please reach out through the repository's issue tracker.

---

**Last Updated**: June 2026
**Repository Status**: Active Development
