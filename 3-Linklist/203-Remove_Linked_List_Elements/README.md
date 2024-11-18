# Remove Elements from Linked List

## Problem Description
This program removes all nodes from a singly linked list where `Node.val` is equal to a given integer `val`. The function returns the modified linked list's head.

### Examples

#### Example 1
**Input:**
- `head = [1,2,6,3,4,5,6]`
- `val = 6`

**Output:**
- `[1,2,3,4,5]`

#### Example 2
**Input:**
- `head = []`
- `val = 1`

**Output:**
- `[]`

#### Example 3
**Input:**
- `head = [7,7,7,7]`
- `val = 7`

**Output:**
- `[]`

---

## Constraints
1. The number of nodes in the linked list is between `0` and `10⁴`.
2. Node values (`Node.val`) are in the range `[1, 50]`.
3. The target value (`val`) is in the range `[0, 50]`.


