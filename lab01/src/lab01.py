import copy
import sys

# ============= Task A =============
print("=" * 30)
print("Task A) Binding / Rebinding")
a = 5
b = a
print("Initial:")
print(f"a = {a}, b = {b}")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")

a = 7
print("After rebinding a = 7:")
print(f"a = {a}, b = {b}")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")

# ============= Task B =============
print("=" * 30)
print("Task B) Mutation vs Rebinding")
a = [1, 2]
b = a
print("Initial:")
print(f"a = {a}")
print(f"b = {b}")

b.append(3)
print("After Mutation:")
print(f"a = {a}")
print(f"b = {b}")
print(f"id(a) == id(b): {id(a) == id(b)}")

# ============= Task C =============
print("=" * 30)
print("Task C) Function arguments")

def mutate_list(l):
    l.append(1)
def rebind_list(l):
    l = [3, 4, 5]

a = []
print("Before call:")
print(f"a = {a}")

mutate_list(a)
print("After mutate_list(a):")
print(f"a = {a}")

rebind_list(a)
print("After rebind_list(a):")
print(f"a = {a}")

# ============= Task D =============
print("=" * 30)
print("Task D) Default argument behavior")


def f(x=[]):
    x.append(1)
    return x

print("1st call:")
print(f())
print("2nd call:")
print(f())

# ============= Task E =============
print("=" * 30)
print("Task E) Copy semantics")
a = [[1, 2]]
b = copy.copy(a)
c = copy.deepcopy(a)

print("Original:")
print(f"a = {a}")

b[0].append(3)
print("After modifying b:")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# ============= Task F =============
print("=" * 30)
print("Task F) Reference counting")

x = []
print(f"getrefcount(x): {sys.getrefcount(x)}")

y = x
print("After y = x: ")
print(f"getrefcount(x): {sys.getrefcount(x)}")

print(f"getrefcount(5): {sys.getrefcount(5)}")
print(f"getrefcount(123456): {sys.getrefcount(123456)}")
