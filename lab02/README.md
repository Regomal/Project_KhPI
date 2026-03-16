# LAB02: Expressions & Control Flow in Python

LAB02 is a university lab project used to practice Python expressions and control flow, demonstrating an understanding
of core language concepts.

The project covers and demonstrates:

- Truthiness evaluation
- Identity vs equality (`is` vs `==`)
- Control flow (`if`, `match`, loops)
- Comprehensions (list and dict)
- Generators and lazy evaluation

---

# Requirements

- Python 3.10+ (strictly required for the `match` statement in Task D)

---

# Repository Structure

lab02/
README.md → this file
requirements.txt → external dependencies (empty for this lab)
src/
lab02.py → source code implementing all tasks
report/
answers.md → short theoretical explanations of Python concepts

---

# Implemented Tasks

All tasks are executed sequentially from the main script.

## Task A: Truthiness

Demonstrates how Python evaluates the truthiness of different objects (`0`, `1`, `[]`, `[1]`, `"hello"`, `None`).

## Task B: Identity vs Equality

Compares `==` and `is` operators across different scenarios (equal values, identical objects, immutable values).

## Task C: Control Flow

Implements a number classification function (`negative`, `zero`, `small positive`, `large positive`) using `if`/`elif`.

## Task D: Pattern Matching

Processes structured events (`click`, `keypress`, `quit`) using Python's structural pattern matching (`match`/`case`).

## Task E: Comprehensions

Generates lists of squares, filtered even squares, and mapped dictionaries using list/dict comprehensions.

## Task F: Generators

Implements a generator function for even numbers and calculates the sum of squares using memory-efficient lazy
evaluation.

---

# Execution

All code should be executed from the root directory of the project.

Command:

    python src/lab02.py

*(Use `python3` instead of `python` depending on your environment).*

Output includes:

- Printed results for Tasks A-F
- Formatted values and their boolean evaluations
- Lazy evaluated calculations without intermediate list creation

---

# Important Notes

- Theoretical answers to the lab questions (e.g., why empty containers evaluate to False, when to use `is`) are located
  in `report/answers.md`.
- Estimated work time for the original lab assignment: 2-3 hours.