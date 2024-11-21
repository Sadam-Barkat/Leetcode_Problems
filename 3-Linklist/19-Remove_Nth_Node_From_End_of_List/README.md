# Remove Nth Node from End of List

## Problem Description

Given the head of a singly linked list, the task is to remove the nth node from the end of the list and return the updated head of the list.

## Examples

### Example 1:
**Input**:  
```plaintext
head = [1, 2, 3, 4, 5], n = 2
Output:

plaintext
Copy code
[1, 2, 3, 5]
Example 2:
Input:

plaintext
Copy code
head = [1], n = 1
Output:

plaintext
Copy code
[]
Example 3:
Input:

plaintext
Copy code
head = [1, 2], n = 1
Output:

plaintext
Copy code
[1]
Constraints
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
