# 1. What is the purpose of type hints in Python?

The main purpose of type hints is to improve code readability and enhance its reliability. They enable the `mypy` tool
to detect type errors before the program runs.

# 2. What is the difference between Any and a generic type T?

`Any`: Disables type checking. Allows any operations to be performed, effectively reverting to dynamic typing (unsafe).

Generic `T`: Maintains strict type checking but makes it flexible. Allows types to be bound (for example, to ensure that
a function returns an object of the same type as the one it received as input).

# 3. What does `Callable[[int], int]` describe?

Describes a callable object (`function`) that takes exactly one argument of type `int` and returns a result of type
`int`.

# 4. Why does mypy --strict require more annotations?

`--strict` prohibits this behavior: it requires that absolutely all functions have explicit annotations for their
arguments and return values, leaving no gray areas in the code.