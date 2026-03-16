# ============= Task A =============
print("=" * 50)
print("Task A) Truthiness")
values = [0, 1, [], [1], "", "hello", None]
for v in values:
    print(f"value: {v} -> {bool(v)}")


# ============= Task B =============
print("=" * 50)
print("Task B) Identity vs Equality")
l1 = [1]
l2 = [1]

print("- equal values but different objects:")
print(f"list1 == list2 -> {l1 == l2}")
print(f"list1 is list2 -> {l1 is l2}")

l3 = l1
print("\n- identical objects:")
print(f"list1 == list3 -> {l1 == l3}")
print(f"list1 is list3 -> {l1 is l3}")


a = 100
b = 100
print("\n- behaviour with immutable values:")
print(f"a == b -> {a == b}")
print(f"a is b -> {a is b}")


# ============= Task C =============
print("=" * 50)
print("Task C) Control Flow")

def describe_number(x):
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    elif 0 < x < 10:
        return "small positive"
    else:
        return "large positive"

values = [-15, 0, 5, 15]
for v in values:
    print(f"{v} -> {describe_number(v)}")
# ============= Task D =============
print("=" * 50)
print("Task D) Pattern Matching")

events = [
    ("click", 10, 20),
    ("keypress", "A"),
    ("quit",)
]

for event in events:
    match event:
        case ("click", x, y):
            print(f"click at {x} {y}")
        case ("keypress", key):
            print(f"key pressed: {key}")
        case ("quit",):
            print("quit event")
        case _:
            print("unknown event")

# ============= Task E =============
print("=" * 50)
print("Task E) Comprehensions")

squares = [x ** 2 for x in range(1, 21)]
print(f"Squares 1 to 20: {squares}")


print(f"Even squares: {[x for x in squares if x % 2 == 0]}")

dict_squares = {x: x ** 2 for x in range(1, 11)}
print(f"Squares 1 to 10: {dict_squares}")

# ============= Task F =============
print("=" * 50)
print("Task F) Generators")

def even_numbers(limit):
    for i in range(0, limit + 1, 2):
        yield i

for num in even_numbers(16):
        print(num, end=" ")
print()

# ============= ADDITIONAL =============
print("=" * 50)
print("Task ADD) Generator expression")
sum_of_squares = sum( (x**2 for x in range(1_000_000) if x % 2 == 0) )
print(f"Sum of squares of even numbers to 1e6:\n{sum_of_squares}")