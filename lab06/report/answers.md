# What is stored in `obj.__dict__`?

It stores the object's internal dictionary, which contains all of its attributes (keys) and their current values (
dictionary values).

# What is the difference between a class and an object?

A class is simply an abstract general concept. An object, on the other hand, is a concrete entity created based on that
design, which actually exists in the program's memory.

# What does `__init__` do?

This is a constructor: it is used to set an object's initial properties when it is created, such as name, job title, age
etc.

# Who calls `__str__`, and when?

When it is needed to convert an object into human-readable text. This happens when we try to print an object using
`print()`, when we use the `str()` function, or when we insert an object into an f-string.

# What is the difference between `==` and `is`?

The `==` operator checks whether the contents of two objects are the same. The `is` operator, on the other hand, checks
whether they are literally the same physical object in the RAM.

# Why do we use `other: object` in `__eq__` and `__lt__`?

Because comparison is a binary operation, and we refer to the object we are comparing the current one with using the
standard term `other`. Why `: object` - because it's the parent of all data types in Python.