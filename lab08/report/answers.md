# PLEASE GIVE US AT LEAST UNTIL SUNDAY TO SUBMIT THE ASSIGNMENT.

### Some of us are desperately short on time because of our German university, and we don’t want to risk losing points since I don’t consider this to be my fault.

# 1. How does a for loop work with custom objects?

It calls `iter()` on our collection, obtains an iterator object, and, in an infinite loop, calls its `__next__()`
method, retrieving elements one by one. As soon as the iterator raises a `StopIteration` exception, the `for` loop
catches it and terminates.

# 2. What methods are required for iteration?

Two methods are required:

* `__iter__()` returns an iterator object

* `__next__()` returns the next element and advances the internal pointer

# 3. How does the with statement work internally?

At the start, `with` calls the object's `__enter__()`, and the result is assigned to the variable after `as`. When
exiting the block, `__exit__()` is automatically called. This is the perfect mechanism to ensure that nothing is
forgotten to be closed

# 4. When is `__exit__` called?

It will always execute at the very end of the `with` block. Even if a severe exception, `return`, or `break` occurs
within the code

# 5. What problem do descriptors solve?

We define the descriptor just once (as a separate class), implement the logic for `__set__` and `__get__` there, and
then simply attach it to the relevant fields—which really helps avoid code duplication

# 6. What happens if a descriptor is not used?

The attributes will remain unvalidated, and we might end up with gems like `student.grade = "watermelon"`, which will
eventually cause a crash

# 7. Why is direct iteration preferred over index-based loops in Python?

Readability, versatility (not all collections have indexes at all—e.g., `set`), performance (they seem to run faster
than index-based lookups)

# Additional Requirement

* **what happens if `StopIteration` is not raised**  
  The `for` loop won't realize that there are no more elements left, and the index will go beyond the bounds of the list
* **what happens if `__exit__` is missing**  
  The `with` block won't even run. Python will check for the method in advance and raise an error immediately.
* **what happens if `validation` is not implemented**  
  Incorrect data types will be passed to the logic, leading to total chaos