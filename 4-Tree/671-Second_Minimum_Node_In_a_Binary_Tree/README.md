# Second Minimum Node in a Special Binary Tree

## Problem Statement

Given a non-empty special binary tree consisting of nodes with non-negative values, where each node in this tree has either exactly two sub-nodes or no sub-nodes. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property `root.val = min(root.left.val, root.right.val)` always holds.

Your task is to output the second minimum value in the set made of all the nodes' values in the whole tree.

If no such second minimum value exists, output `-1`.

## Examples

### Example 1:

**Input:**
```
root = [2,2,5,null,null,5,7]
```

**Output:**
```
5
```

**Explanation:**
The smallest value is `2`, and the second smallest value is `5`.

---

### Example 2:

**Input:**
```
root = [2,2,2]
```

**Output:**
```
-1
```

**Explanation:**
The smallest value is `2`, but there isn't any second smallest value.

---

## Constraints

- The number of nodes in the tree is in the range `[1, 25]`.
- `1 <= Node.val <= 2^{31} - 1`
- `root.val == min(root.left.val, root.right.val)` for each internal node of the tree.