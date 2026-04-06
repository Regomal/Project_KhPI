from typing import Callable, Any, TypeVar, cast
from agent import Agent

F = TypeVar('F', bound=Callable[..., Any])


def task_block(title: str) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print("=" * 50)
            print(title)
            result = func(*args, **kwargs)
            print("=" * 50, end="\n\n")
            return result

        return cast(F, wrapper)

    return decorator


# ============= Task A =============
@task_block("Task A) Define the class")
def task_a(a : Agent) -> None:
    print(f"Name: {a.name}")
    print(f"Position: {a.position}")
    print(f"Age: {a.age}")
    print(f"Gender: {'W' if a.gender else 'M'}")


# ============= Task B =============
@task_block("Task B) Inspect internal structure")
def task_b(a : Agent) -> None:
    print(f"Original: {a.__dict__}")
    a.__dict__['age'] = 42
    print(f"Changed: {a.__dict__}")


# ============= Task C =============
@task_block("Task C) Implement __str__")
def task_c(a : Agent) -> None:
    print(f"str({a.name}) -> {str(a)}")


# ============= Task D =============
@task_block("Task D) Implement __repr__")
def task_d(a : Agent) -> None:
    print(f"repr({a.name}) -> {repr(a)}")


# ============= Task E =============
@task_block("Task E) Implement equality (__eq__)")
def task_e(a2: Agent, a21: Agent, a3: Agent) -> None:

    print(f"a2 == a21 (identical) -> {a2 == a21}")
    print(f"a2 == a3 (different) -> {a2 == a3}")
    print(f"a2 == 'string' -> {a2 == 'string'}")


# ============= Task F =============
@task_block("Task F) Implement ordering (__lt__)")
def task_f(a1: Agent, a2: Agent) -> None:
    print(f"a2 ({a2.position}) < a1 ({a1.position}) -> {a2 < a1}")

    try:
        a2 < "Something"
    except TypeError as e:
        print(f"Caught expected error -> {e}")


# ============= Task G =============
@task_block("Task G) Sorting")
def task_g(agents : list[Agent]) -> None:
    print("Before sort:")
    for a in agents:
        print(f" - {a}")

    agents.sort(reverse=True)

    print("\nAfter sort by Position:")
    for a in agents:
        print(f" - {a}")

    agents.sort(key=lambda x: x.name)
    print("\nAfter sort alphabetically:")
    for a in agents:
        print(f" - {a}")


def main() -> None:
    a1  = Agent("Teresa Lisbon", "senior agent", 36, True)
    a2  = Agent("Patrick Jane", "consultant", 39, False)
    a21 = Agent("Patrick Jane", "consultant", 39, False)
    a3  = Agent("Wayne Rigsby", "operative", 30, False)
    a4  = Agent("Grace Van Pelt", "analyst", 25, True)
    a5  = Agent("Kimball Cho", "operative", 35, False)


    task_a(a1)

    task_b(a1)

    task_c(a3)

    task_d(a3)

    task_e(a2, a21, a4)

    task_f(a1, a2)

    agents = [a1, a2, a3, a4, a5]
    task_g(agents)


if __name__ == "__main__":
    main()