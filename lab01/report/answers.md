# Task A

Names are simply **labels** (bindings) for objects. When I write a = 7, I simply attach the name “a” to a new object,
while
the old value 5 remains unchanged. Therefore, b continues to refer to the **old value**.

# Task B

Both names look at the same list. Mutation changes the internals of this list, so the changes are visible through both
names. Rebinding, on the other hand, would simply detach the label from the old list and attach it to the new one.

# Task C

When we pass an argument, it is not copied, but simply bound to the parameter. If we mutate the list inside the
function, it changes outside as well. But parameters are new local names. If we reassign the parameter inside, we simply
attach a local label to the new object, and the external list remains untouched.

# Task D

The list grows because default values are created (calculated) only once—when the function is defined. Because of this,
the same object is used and reused for all calls.

# Task E

A shallow copy creates a new external list, but the nested objects still remain references to the old data. A deep copy
recursively/cascadingly (what a cool word) clones everything, including nested lists, creating a completely independent
copy.

# Task F

In 5, this counter is due to optimization. Small numbers are cached immediately at startup and are immortal objects. 

### God bless deepl.com