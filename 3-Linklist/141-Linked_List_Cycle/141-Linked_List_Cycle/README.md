# Linked List Cycle Detection

## Problem Description
Given the `head` of a linked list, determine if the linked list contains a cycle. A cycle exists if there is a node in the list that can be revisited by continuously following the `next` pointers. 

If there is a cycle, return `true`; otherwise, return `false`.

### Example Scenarios

#### Example 1
**Input:** `head = [3,2,0,-4]`, `pos = 1`  
**Output:** `true`  
**Explanation:** The tail node connects to the 1st node, creating a cycle.

#### Example 2
**Input:** `head = [1,2]`, `pos = 0`  
**Output:** `true`  
**Explanation:** The tail node connects to the 0th node, creating a cycle.

#### Example 3
**Input:** `head = [1]`, `pos = -1`  
**Output:** `false`  
**Explanation:** There is no cycle in the linked list.

### Constraints
- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is either `-1` (indicating no cycle) or a valid index in the linked list.


