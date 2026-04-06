# LAB06: Python Object Model and Basic Object Behavior

LAB06 is a university lab project designed to practice implementing a custom Python class and gradually transforming it into a well-behaved object that integrates seamlessly with the Python language.

The project covers and demonstrates:

- Working with classes and objects
- Understanding how internal attributes are stored (`__dict__`)
- Implementing basic dunder (magic) methods (`__str__`, `__repr__`, `__eq__`, `__lt__`)
- Controlling object behavior in Python (e.g., natural ordering and sorting)
- Writing type-safe object-oriented code with `mypy --strict`

---

## Requirements

- Python 3.10+ (Required for modern type annotations)

---

## Environment Setup

To ensure the project runs cleanly and static analysis tools function correctly, use a virtual environment. The `mypy` static type checker must be installed.

**1. Create a virtual environment:**
Open your terminal in the root of the project (the `lab06` folder) and run:

    python -m venv venv

*(Use `python3` instead of `python` depending on your OS).*

**2. Activate the virtual environment:**

- On **Windows**:

  venv\Scripts\activate

- On **macOS / Linux**:

  source venv/bin/activate

**3. Install dependencies:**
Once the virtual environment is active, install the required packages (this will install `mypy` and any other requirements):

    pip install -r requirements.txt

*Note: Ensure your `requirements.txt` contains the word `mypy` on a new line.*

---

## Repository Structure

    lab06/
    ├── README.md           → this file
    ├── requirements.txt    → external dependencies (must include mypy)
    ├── src/
    │   ├── agent.py        → contains the `Agent` class and its dunder methods
    │   └── main.py         → source code containing the execution of all tasks
    └── report/
        └── answers.md      → short explanations and answers to theoretical questions

---

## Implemented Tasks

All tasks are executed sequentially from the `main.py` script. The entire codebase is strictly typed and separated into business logic (`agent.py`) and execution tests (`main.py`).

- **Task A: Define the class**
  Creates an `Agent` class with attributes (name, position, age, gender) initialized via `__init__`.
- **Task B: Inspect internal structure**
  Demonstrates how attributes are stored by accessing and modifying the object's `__dict__` directly.
- **Task C: Implement `__str__`**
  Defines a user-friendly, human-readable string representation of the object.
- **Task D: Implement `__repr__`**
  Defines a formal, developer-oriented representation useful for debugging.
- **Task E: Implement equality (`__eq__`)**
  Teaches the object how to compare itself with others by checking all field values and handling incompatible types safely.
- **Task F: Implement ordering (`__lt__`)**
  Defines custom logic for the `<` operator, allowing objects to be compared based on their position rank.
- **Task G: Sorting**
  Demonstrates deep integration with Python by sorting a list of objects natively using the implemented `__lt__` method.

---

## Execution

Ensure your virtual environment is activated. There are two parts to running this project:

**1. Static Type Checking (Mypy)**
Before running the code, verify that the project passes strict type checking. Run the following command from the root directory:

    mypy --strict src/

*Expected Output:* The command must complete without errors (e.g., `Success: no issues found in 2 source files`).

**2. Running the Code**
Run the main script to see the actual output:

    python src/main.py

*Expected Output:*
- Program running without errors.
- Console logs demonstrating the correct results for Tasks A through G, clearly separated by headers.

---

## Important Notes

- Short explanations and answers to theoretical questions about Python objects and dunder methods are located in `report/answers.md`.