# Remove Nodes with Greater Values on the Right

## Problem Description

You are given the head of a **singly linked list**.  
Your task is to remove every node in the list that has a node with a greater value to its **right**.  

Return the head of the modified linked list.

---

## Examples

### Example 1:
**Input:**  
`head = [5, 2, 13, 3, 8]`  
**Output:**  
`[13, 8]`  

**Explanation:**  
- Node 13 is greater than 5 and 2 on its right, so 5 and 2 are removed.  
- Node 8 is greater than 3 on its right, so 3 is removed.  
- Nodes 13 and 8 remain.

---

### Example 2:
**Input:**  
`head = [1, 1, 1, 1]`  
**Output:**  
`[1, 1, 1, 1]`  

**Explanation:**  
All nodes have the same value, so no nodes are removed.

---

## Constraints

1. The number of nodes in the linked list is in the range **[1, 10⁵]**.
2. Each node's value is in the range **[1, 10⁵]**.
