from typing import Callable, TypeVar

# ============= Task A =============
print("=" * 50)
print("Task A) Basic Type Hints")

def add(a: int, b: int) -> int:
    return a + b

def square_list(data: list[int]) -> list[int]:
    return [x * x for x in data]

print(f"add(5, 3) -> {add(5, 3)}")

lst_a = [1, 2, 3]
print(f"List: {lst_a}")
print(f"square_list({lst_a}) -> {square_list(lst_a)}")

print("=" * 50, end="\n\n")


# ============= Task B =============
print("=" * 50)
print("Task B) Typed Collections")

def filter_even(data: list[int]) -> list[int]:
    return [x for x in data if x % 2 == 0]

lst_b = [1, 2, 3, 4, 5]
print(f"List: {lst_b}")
print(f"filter_even({lst_b}) -> {filter_even(lst_b)}")

print("=" * 50, end="\n\n")


# ============= Task C =============
print("=" * 50)
print("Task C) Optional")

def find(data: list[int], x: int) -> int | None:
    if x in data:
        return x
    return None

lst_c = [10, 20, 30]
print(f"List: {lst_c}")
print(f"find 20: {find(lst_c, 20)}")
print(f"find 42: {find(lst_c, 42)}")

print("=" * 50, end="\n\n")


# ============= Task D =============
print("=" * 50)
print("Task D) Function Type")

def apply(func: Callable[[int], int], x: int) -> int:
    return func(x)

def double(n: int) -> int:
    return n * 2

def increment(n: int) -> int:
    return n + 1

val_d = 5
print(f"Value: {val_d}")
print(f"apply(double, {val_d}) -> {apply(double, val_d)}")
print(f"apply(increment, {val_d}) -> {apply(increment, val_d)}")

print("=" * 50, end="\n\n")


# ============= Task E =============
print("=" * 50)
print("Task E) Generics")

T = TypeVar('T')

def first(items: list[T]) -> T:
    return items[0]

lst_e1 = [100, 200, 300]
lst_e2 = ["apple", "banana"]
print(f"List 1: {lst_e1}")
print(f"first({lst_e1}) -> {first(lst_e1)}")
print(f"List 2: {lst_e2}")
print(f"first({lst_e2}) -> {first(lst_e2)}")

print("=" * 50, end="\n\n")


# ============= Task F =============
print("=" * 50)
print("Task F) Function Returning Function")

def make_multiplier(k: int) -> Callable[[int], int]:
    def multiplier(n: int) -> int:
        return n * k
    return multiplier

fun_f = make_multiplier(3)
val_f = 10
print(f"make_multiplier(3) to {val_f} -> {fun_f(val_f)}")

print("=" * 50, end="\n\n")


# ============= Task G =============
print("=" * 50)
print("Task G) Pipeline")

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Original: {nums}")

evens = filter(lambda x: x % 2 == 0, nums)
squares = (x * x for x in evens)
result = sum(squares)

# result = sum((x * x for x in filter(lambda x: x % 2 == 0, nums)))

print(f"Result -> {result}")

print("=" * 50, end="\n\n")