# Detect Cycle in a Linked List

## Problem Description
This program determines if a given singly linked list contains a cycle. A cycle occurs when a node's `next` pointer links to a previous node in the list, forming a loop. If a cycle is detected, the function returns `true`; otherwise, it returns `false`.

### Examples

#### Example 1
**Input:**
- `head = [3,2,0,-4]`
- `pos = 1`

**Output:** 
- `true`

**Explanation:**  
The tail connects to the 1st node (0-indexed), creating a cycle in the list.

#### Example 2
**Input:**
- `head = [1,2]`
- `pos = 0`

**Output:** 
- `true`

**Explanation:**  
The tail connects to the 0th node, creating a cycle.

#### Example 3
**Input:**
- `head = [1]`
- `pos = -1`

**Output:** 
- `false`

**Explanation:**  
No cycle exists in the linked list.

---

## Constraints
1. The number of nodes in the linked list is in the range `[0, 10⁴]`.
2. Node values (`Node.val`) are in the range `[-10⁵, 10⁵]`.
3. `pos` is either `-1` (indicating no cycle) or a valid index in the linked list.

