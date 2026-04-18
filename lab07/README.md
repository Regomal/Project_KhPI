# LAB07: Behavior, Protocols, ABC, Dataclasses, Slots

LAB07 is a university lab project designed to explore different ways to define and implement behavior in Python. The
goal is to understand how Python defines "type" through behavior rather than strict inheritance.

The project covers and demonstrates:

- Structural typing and Duck typing
- Defining explicit behaviors using `Protocol`
- Reducing boilerplate code using `@dataclass`
- Restricting object structure and optimizing memory using `slots`
- Enforcing explicit contracts using Abstract Base Classes (ABC)
- Writing type-safe object-oriented code with `mypy --strict`

---

## Requirements

- Python 3.10+ (Required for modern type annotations and modern dataclass features)

---

## Environment Setup

To ensure the project runs cleanly and static analysis tools function correctly, use a virtual environment. The `mypy`
static type checker must be installed.

**1. Create a virtual environment:**
Open your terminal in the root of the project (the `lab07` folder) and run:

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

    lab07/
    ├── README.md           → this file
    ├── requirements.txt    → external dependencies (must include mypy)
    ├── src/
    │   └── main.py         → source code containing the execution of all tasks
    └── report/
        └── answers.md      → short explanations and answers to theoretical questions

---

## Implemented Tasks

All tasks are executed sequentially from the `main.py` script. The entire codebase is strictly typed and demonstrates a
single concept: an object that can be serialized, implemented using different approaches.

- **Preparation: Protocol and Helper Function**
  Defines a `Serializable` Protocol and a universal `export()` function to demonstrate structural typing.
- **Task A: Regular class (Duck typing)**
  Creates a standard class without inheritance that seamlessly works with the Protocol.
- **Task B: Dataclass implementation**
  Replaces the standard class with a `@dataclass` to achieve the exact same behavior with less boilerplate code.
- **Task C: Slots**
  Uses `@dataclass(slots=True)` to demonstrate how slots restrict the object's structure, disable dynamic dictionaries (
  `__dict__`), and prevent the addition of unexpected attributes.
- **Task D: ABC version**
  Defines an Abstract Base Class (`SerializableABC`) and a concrete implementation to demonstrate nominal typing,
  explicit inheritance, and how it differs from a Protocol.

---

## Execution

Ensure your virtual environment is activated. There are two parts to running this project:

**1. Static Type Checking (Mypy)**
Before running the code, verify that the project passes strict type checking. Run the following command from the root
directory:

    mypy --strict src/main.py

*Expected Output:* The command must complete without errors.

**2. Running the Code**
Run the main script to see the actual output:

    python src/main.py

*Expected Output:*

- Program running without errors.
- Console logs demonstrating the correct results for Tasks A through D, separated by headers.
- Short explanations included in the output answering "What do we see?" and "Why does it work?".

---

## Important Notes

- Short explanations, comparisons of approaches (Protocol vs. ABC), limitations, and answers to theoretical questions
  are located in `report/answers.md`.