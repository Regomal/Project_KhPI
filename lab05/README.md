# LAB05: Type Hints, Generics, Mypy

LAB05 is a university lab project designed to practice using type hints and to understand how static typing improves code reliability and clarity.

The project covers and demonstrates:

- Basic type annotations for functions
- Typed collections (`list[int]`)
- Generics using `TypeVar`
- Function types and functions returning functions (`Callable`)
- Strict static type checking with `mypy`
- Functional processing pipelines

---

## Requirements

- Python 3.11 (Required for `TypeVar` from the `typing` module and `|` union syntax)

---

## Environment Setup

To ensure the project runs cleanly and static analysis tools function correctly, use a virtual environment. The `mypy` static type checker must be installed.

**1. Create a virtual environment:**
Open your terminal in the root of the project (the `lab05` folder) and run:

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

    lab05/
    ├── README.md           → this file
    ├── requirements.txt    → external dependencies (must include mypy)
    ├── src/
    │   └── main.py         → source code containing the implementation of the tasks
    └── report/
        └── answers.md      → short explanations and answers to theoretical questions

---

## Implemented Tasks

All tasks are executed sequentially from the main script. The entire codebase is strictly typed.

- **Task A: Basic Type Hints**
  Adds basic type annotations to simple addition and list comprehension functions.
- **Task B: Typed Collections**
  Implements a function that strictly accepts and returns a `list[int]`, keeping only even numbers.
- **Task C: Optional**
  Demonstrates the use of `int | None` for a search function that might not find a value.
- **Task D: Function Type**
  Uses `Callable[[int], int]` to correctly type hint a function passed as an argument.
- **Task E: Generics**
  Utilizes `TypeVar` to create a generic function capable of returning the first element of a list of any type while preserving type safety.
- **Task F: Function Returning Function**
  Implements a closure returning a `Callable` multiplier.
- **Task G: Pipeline**
  Creates a data processing pipeline using lambda expressions and generator expressions to filter, square, and sum a list of numbers.

---

## Execution

Ensure your virtual environment is activated. There are two parts to running this project:

**1. Static Type Checking (Mypy)**
Before running the code, verify that the project passes strict type checking. Run the following command from the root directory:

    mypy --strict src/

*Expected Output:* The command must complete without errors (e.g., `Success: no issues found in 1 source file`).

**2. Running the Code**
Run the main script to see the actual output:

    python src/main.py

*Expected Output:*
- Programs running without errors.
- Console logs demonstrating the correct results for Tasks A through G.

---

## Important Notes

- Short explanations and answers to theoretical questions about Python typing are located in `report/answers.md`.
- Estimated work time: 2-3 hours.