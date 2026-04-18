from typing import Callable, Any, TypeVar, cast, Type, List, Optional
from types import TracebackType


# ==========================================================
# Wrapper
# ==========================================================

F = TypeVar('F', bound=Callable[..., Any])
def task_block(title: str) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print("=" * 118)
            print("----- " + title + " -----")
            result = func(*args, **kwargs)
            print("=" * 118, end="\n\n")
            return result
        return cast(F, wrapper)
    return decorator



# ==========================================================
# Task C: Descriptor
# ==========================================================
class GradeValidator:

    def __init__(self) -> None:
        self.private_name = ""

    def __set_name__(self, owner: Type[Any], name: str) -> None:

        self.private_name = "_" + name

    def __get__(self, obj: Any, objtype: Any = None) -> Any:
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj: Any, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Grade must be an integer from 0 to 100.")
        if not (0 <= value <= 100):
            raise ValueError(f"Grade {value} is invalid. Must be integer between 0 and 100.")
        setattr(obj, self.private_name, value)



# ==========================================
# Data Setup
# ==========================================
class Student:
    grade = GradeValidator()

    def __init__(self, name: str, group: str, grade: int) -> None:
        self.name = name
        self.group = group
        self.grade = grade

    def __str__(self) -> str:
        return f"Student: {self.name}, Group: {self.group}, Grade: {self.grade}"


# ==========================================
# Task A: Iteration (Iterator)
# ==========================================
class StudentIterator:

    def __init__(self, students: List[Student]) -> None:
        self._students = students
        self._index = 0

    def __iter__(self) -> 'StudentIterator':
        return self

    def __next__(self) -> Student:
        if self._index >= len(self._students):
            raise StopIteration

        student = self._students[self._index]
        self._index += 1
        return student


# ==========================================
# Task B: Context Manager
# ==========================================
class StudentCollection:

    def __init__(self, students: List[Student]) -> None:
        self._students = students

    def __iter__(self) -> StudentIterator:
        return StudentIterator(self._students)

    def __enter__(self) -> 'StudentCollection':
        print("\n--- Entering the context ---")
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        if exc_type is not None:
            print(f"--- Exiting the context (with error: {exc_type.__name__}) ---")
        else:
            print("--- Exiting the context ---")


# ==========================================
# Task D: Integration
# ==========================================
@task_block("Task A — Iteration")
def task_a(students_data : List[Student]) -> None:
    collection = StudentCollection(students_data)
    for student in collection:
        print(student)

    print("""
    What?
    A list of all students printed one by one.
    Why?
    The 'for' loop calls __iter__() on StudentCollection,
    which returns a StudentIterator. The loop then calls __next__() until StopIteration""")

@task_block("Task B — Context Manager")
def task_b(students_data : List[Student]) -> None:
    with StudentCollection(students_data) as ctx_collection:
        for student in ctx_collection:
            print(f"{student.name} - {student.grade}/100")

    print("""
    What? 
    Enter message, grades printed, then normal Exit message.
    Why? 
    The `with` statement invokes __enter__(), assigns the object to 'ctx_collection',
    and guarantees __exit__() is called at the end of the block.""")

@task_block("Task C — Descriptor")
def task_c() -> None:
    try:
        print("Assign grade 4242")
        Student("Roma M.", "KN-124", 4242)
    except ValueError as e:
        print(f"Validation Error caught: {e}")

    print("""
    What?
    The program blocks the invalid assignment and throws a ValueError.
    Why? 
    Assigning to 'self.grade' triggers the GradeValidator.__set__() method, 
    which checks the constraints before storing the value.""")


def main() -> None:
    students_data = [
        Student("Gleb R.", "KN-124", 87),
        Student("Gleb G.", "KN-124", 86),
        Student("Vlad S.", "KN-124", 91),
        Student("Katya B.", "KN-124", 96),
        Student("Sonya L.", "KN-124", 100),
    ]

    task_a(students_data)

    task_b(students_data)

    task_c()

if __name__ == "__main__":
    main()