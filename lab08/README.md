# LAB 08: Iteration, Context Managers, and Descriptors

LAB 08 is a university lab project designed to implement a custom object that integrates deeply with Python through its
core protocols. The primary goal is to understand that built-in Python behavior (such as loops, the `with` statement,
and attribute assignment) is driven by protocols implemented via special ("magic") methods.

The project covers and demonstrates:

- Implementing the Iteration protocol using `__iter__`, `__next__`, and `StopIteration`
- Managing resources and execution flow using Context Managers (`__enter__` and `__exit__`)
- Intercepting and validating attribute access using Descriptors (`__get__`, `__set__`, and `__set_name__`)
- Writing type-safe object-oriented code with `mypy --strict`

---

## Requirements

- Python 3.10+ (Required for modern type annotations and `__set_name__` descriptor behavior)

---

## Environment Setup

To ensure the project runs cleanly and static analysis tools function correctly, use a virtual environment. The `mypy`
static type checker must be installed.

**1. Create a virtual environment:**
Open your terminal in the root of the project (the `lab08` folder) and run:

    python -m venv venv

*(Use `python3` instead of `python` depending on your OS).*

**2. Activate the virtual environment:**

- On **Windows**:

  venv\Scripts\activate

- On **macOS / Linux**:

  source venv/bin/activate

**3. Install dependencies:**
Once the virtual environment is active, install the required packages (this will install `mypy`):

    pip install -r requirements.txt

*Note: Ensure your `requirements.txt` contains the word `mypy` on a new line.*

---

## Repository Structure

    lab08/
    ├── README.md           → this file
    ├── requirements.txt    → external dependencies (must include mypy)
    ├── src/
    │   └── your_code/
    │       └── main.py     → source code containing the execution of all tasks
    └── report/
        └── answers.md      → short explanations and answers to theoretical questions

---

## Implemented Tasks

All tasks are executed sequentially from the `main.py` script. The entire codebase is strictly typed and built
step-by-step around a `Student` data structure.

- **Data Setup**
  Creates a standard `Student` class and initializes a list of realistic student records.
- **Task A: Iteration**
  Creates a `StudentCollection` and a dedicated `StudentIterator`. It demonstrates how to implement the iterator
  protocol to allow direct `for` loop traversal without index-based loops.
- **Task B: Context Manager**
  Extends `StudentCollection` to support the `with` statement, logging entry and exit events, and proving that
  `__exit__` is called even when exceptions occur.
- **Task C: Descriptor**
  Implements a `GradeValidator` descriptor to enforce business rules (grades must be between 0 and 100). It
  automatically rejects invalid values during attribute assignment.
- **Task D: Integration**
  Combines all components, demonstrating a `StudentCollection` being iterated over inside a `with` block, while safely
  reading validated attributes.

---

## Execution

Ensure your virtual environment is activated. There are two parts to running this project:

**1. Static Type Checking (Mypy)**
Before running the code, verify that the project passes strict type checking. Run the following command from the root
directory:

    mypy --strict src/your_code/main.py

*Expected Output:* The command must complete without errors. This is a strict grading requirement.

**2. Running the Code**
Run the main script to see the actual output:

    python src/your_code/main.py

*