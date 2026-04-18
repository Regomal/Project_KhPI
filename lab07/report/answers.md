# 1. What is duck typing?

We don't look at the object's type; we check whether it has the required method.  
If we accidentally pass an object whose method has a different name or is missing, the program will crash with an
`AttributeError`

# 2. How does Protocol differ from ABC?

Protocol - structural: we only care about the presence of methods in the class; inheritance is not required. ABC
explicit: a class must explicitly inherit from a parent to be considered compatible.

# 3. Does Protocol require inheritance? Why or why not?

No, it doesn't. The protocol checks the structure from the outside. You can write a function that works with any object,
as long as it supports the required behavior.

# 4. What problem does ABC solve?

ABC solves the problem of control and standardization. It ensures that every derived class must implement all abstract
methods.  
**Lim:** If even one abstract method is not implemented, the program will crash

# 5. What does @dataclass generate automatically?

Routine dunders: it automatically generates methods such as `__init__`, `__repr__`, `__eq__` etc. to reduce templated
code

# 6. What changes when using slots?

A fixed amount of memory is allocated for attributes, and the dynamic dictionary for each object is no longer used.  
**Lim:** You can no longer create fields on the fly; you can only work with the ones that were defined when the class
was created.

# 7. Why does Protocol work with different implementations (regular class, dataclass, slots)?

The only thing that matters is the object's final interface. Regardless of how the class is implemented, if the
resulting instance has a `serialize()` method, it satisfies the requirements of the Protocol