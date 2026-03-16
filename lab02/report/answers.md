# Task A

A container with a length of zero → zero useful data. This is equivalent to `False` in a Boolean context.  
To put it more technically, the containers implement methods that explicitly instruct the interpreter to treat a length
of 0 as a false value.

# Task B

`is` is used to verify that two variables refer to the same object in memory. The most obvious example is the comparison
`is None`. `==` is used to compare values, even though they may be different objects.

# Task D

Match is convenient because it can immediately check the structure and format of the data (such as the length of a tuple
and the type of its elements) and immediately unpack those values into variables

# Task F

1. `List comprehension` evaluates and creates the entire list in memory at once. `Generator expression` does not create
   the entire collection, but returns a generator object that yields elements one at a time, which allows for efficient
   memory usage.
2. Why are generators considered lazy?
   Generators are called “lazy” because they defer computations until the value is actually needed. Instead of
   generating all the data in advance, a generator computes only the next element when it is accessed and then goes to
   sleep until the next request.
3. When the generator has exhausted all its values (encounters a `return`), it throws a built-in `StopIteration`
   exception and - as surprising as it may sound - stops generating values.

### God bless deepl.com again