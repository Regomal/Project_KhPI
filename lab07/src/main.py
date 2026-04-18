from typing import Callable, Any, TypeVar, cast, Protocol
from dataclasses import dataclass
from abc import ABC, abstractmethod

# ==========================================================
# Wrapper
# ==========================================================
F = TypeVar('F', bound=Callable[..., Any])
def task_block(title: str) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print("=" * 118)
            print("-----" + title + "-----")
            result = func(*args, **kwargs)
            print("=" * 118, end="\n\n")
            return result
        return cast(F, wrapper)
    return decorator


# ==========================================================
# Preparation
# ==========================================================
class Serializable(Protocol):
    def serialize(self) -> str:
        ...


def export(obj: Serializable) -> None:
    print(obj.serialize())


# ==========================================================
# Task A: Regular Class (Duck Typing)
# ==========================================================
class StudentRegular:
    def __init__(self, name: str, group: str, av_grade: float) -> None:
        self.name = name
        self.group = group
        self.av_grade = av_grade

    def serialize(self) -> str:
        return f"[A: Regular] Student: {self.name}, Group: {self.group}, GPA: {self.av_grade}"


@task_block("Task A: Regular class (duck typing)")
def task_a() -> None:
    student_a = StudentRegular("Gleb R.", "KN-124", 4.38)
    export(student_a)

    print("""
    What?
    A regular class is successfully passed to the `export` function
    Why?
    Thanks to duck typing: the class implements the `serialize()` method,
    and that is sufficient to satisfy the Serializable protocol""")


# ==========================================================
# Task B: Dataclass
# ==========================================================
@dataclass
class StudentData:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"[B: Dataclass] Student: {self.name}, Group: {self.group}, GPA: {self.average_grade}"


@task_block("Task B: Dataclass")
def task_b() -> None:
    student_b = StudentData("Gleb G.", "KN-124", 4.33)
    export(student_b)

    print("""
    What?
    A dataclass works exactly the same way as a regular class
    Why? 
    The dataclass automatically generated an `__init__` method,
    maintaining compatibility with the Serializable protocol because it has a `serialize` method""")


# ==========================================================
# TASK C: Slots
# ==========================================================
@dataclass(slots=True)
class StudentSlots:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"[C: Slots] Student: {self.name}, Group: {self.group}, GPA: {self.average_grade}"

# Yes mypy complains about this but that's exactly how it's supposed to be
def add_field(s: StudentSlots | StudentRegular) -> None:
    try:
        s.age = 19
        print(f"Field is successfully added: ", end="")
        print(s.serialize() + f", age: {s.age}")
    except AttributeError as e:
        print(f"Expected Error: {e}")


@task_block("Task C: Dataclass")
def task_c() -> None:
    student_c1 = StudentSlots("Katya B.", "KN-124", 4.78)
    student_c2 = StudentRegular("Sonya L.", "KN-124", 5.0)

    export(student_c1)
    export(student_c2)

    add_field(student_c1)
    add_field(student_c2)

    print("""
    What?
    The object displays data but does not allow adding a new field
    Why?
    Slots constrain the object's structure, saving memory,
    but the serialize() method remains available to the protocol""")


# ==========================================================
# Task D: ABC Version
# ==========================================================

class SerializableABC(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass


class StudentABC(SerializableABC):
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def serialize(self) -> str:
        return f"[D: ABC] Student: {self.name}, Group: {self.group}, GPA: {self.average_grade}"


@task_block("Task D: ABC")
def task_d() -> None:
    student_d = StudentABC("Vlad S.", "KN-124", 4.44)
    export(student_d)

    print("""
    What?
    A class that inherits from ABC is also accepted by the export function
    Why?
    The object adheres to both explicit inheritance (ABC) and structural inheritance (Protocol)""")


def main() -> None:
    task_a()

    task_b()

    task_c()

    task_d()


if __name__ == "__main__":
    main()
