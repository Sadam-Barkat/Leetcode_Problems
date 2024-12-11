# Kth Smallest Element in a Binary Search Tree

## Problem Statement

Given the root of a binary search tree and an integer `k`, return the `k`th smallest value (1-indexed) among all the values of the nodes in the tree.

## Examples

### Example 1:

**Input:** 
```
root = [3,1,4,null,2], k = 1
```

**Output:** 
```
1
```

**Explanation:**

Visual representation of the tree:
```
      3
     / \
    1   4
     \
      2
```
The in-order traversal of this tree yields `[1, 2, 3, 4]`. The 1st smallest value is `1`.

### Example 2:

**Input:** 
```
root = [5,3,6,2,4,null,null,1], k = 3
```

**Output:** 
```
3
```

**Explanation:**

Visual representation of the tree:
```
        5
       / \
      3   6
     / \
    2   4
   /
  1
```
The in-order traversal of this tree yields `[1, 2, 3, 4, 5, 6]`. The 3rd smallest value is `3`.

## Constraints

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4