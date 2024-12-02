# LeetCode Problem: Maximum Depth of Binary Tree

## Description
Given the root of a binary tree, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root to the farthest leaf node.

### Examples:
1. **Input**:  
Copy code
3
/
9 20 /
15 7

markdown
Copy code
   **Output**: `3`

2. **Input**: `root = []`  
   **Output**: `0`

## Constraints:
- Number of nodes: `[0, 10⁴]`
- Node values: `-100 <= Node.val <= 100`

---

## Approach
- If `root` is `None`, return `0`.
- Recursively compute the depth of left and right subtrees.
- Maximum depth = `1 + max(left_depth, right_depth)`.

## Complexity
- **Time**: `O(n)` (visit each node once).
- **Space**: `O(h)` (height of the tree due to recursion).