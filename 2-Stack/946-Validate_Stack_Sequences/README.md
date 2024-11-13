# Stack Sequence Validation

This problem involves determining if a given sequence of `push` and `pop` operations on an initially empty stack could produce a given `popped` sequence from a `pushed` sequence of integers.

## Problem Description

You are given two integer arrays `pushed` and `popped`, each containing distinct values. Both arrays represent sequences where:
- `pushed` indicates the order in which integers are pushed onto the stack.
- `popped` represents the intended order of integers to be popped from the stack.

The task is to determine if this `popped` order could be a valid result of stack operations on `pushed`. Return `true` if it is possible, or `false` otherwise.

### Examples

#### Example 1

**Input:**
```plaintext
pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
Output:

plaintext
Copy code
true
Explanation: The sequence of stack operations could be:

push(1), push(2), push(3), push(4), then pop() (4 is popped).
push(5), then pop() (5 is popped), pop() (3 is popped), pop() (2 is popped), pop() (1 is popped). The resulting popped order is [4, 5, 3, 2, 1].
Example 2
Input:

plaintext
Copy code
pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
Output:

plaintext
Copy code
false
Explanation: Here, 1 cannot be popped before 2 if we are following stack operations with pushed as the input order.

Constraints
1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.