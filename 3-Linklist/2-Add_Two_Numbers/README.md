# Add Two Numbers (Linked List)

## Problem Description

You are given two non-empty linked lists representing two non-negative integers.  
The digits are stored in reverse order, and each of their nodes contains a single digit.  

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

## Examples

### Example 1:
**Input:**  
`l1 = [2,4,3]`, `l2 = [5,6,4]`  
**Output:**  
`[7,0,8]`  

**Explanation:**  
The numbers represented are `342` and `465`. Their sum is `807`, which is returned as `[7,0,8]`.

---

### Example 2:
**Input:**  
`l1 = [0]`, `l2 = [0]`  
**Output:**  
`[0]`

---

### Example 3:
**Input:**  
`l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`  
**Output:**  
`[8,9,9,9,0,0,0,1]`  

**Explanation:**  
The numbers represented are `9999999` and `9999`. Their sum is `10009998`, which is returned as `[8,9,9,9,0,0,0,1]`.

---

## Constraints

1. The number of nodes in each linked list is in the range `[1, 100]`.
2. `0 <= Node.val <= 9`.
3. It is guaranteed that the list represents a number that does not have leading zeros.
