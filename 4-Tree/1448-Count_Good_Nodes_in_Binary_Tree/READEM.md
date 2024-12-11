# Good Nodes in Binary Tree

## Problem Statement

Given a binary tree root, a node `X` in the tree is named *good* if, in the path from the root to `X`, there are no nodes with a value greater than `X`.

Your task is to return the number of good nodes in the binary tree.

### Example 1:

**Input:**
root = [3,1,4,3,null,1,5]

makefile
Copy code

**Output:**
4

yaml
Copy code

**Explanation:**
- Nodes in blue are good.
- Root node (3) is always a good node.
- Node 4 → (3, 4) is the maximum value in the path starting from the root.
- Node 5 → (3, 4, 5) is the maximum value in the path.
- Node 3 → (3, 1, 3) is the maximum value in the path.

---

### Example 2:

**Input:**
root = [3,3,null,4,2]

makefile
Copy code

**Output:**
3

yaml
Copy code

**Explanation:**
- Node 2 → (3, 3, 2) is not good because "3" is higher than it.

---

### Example 3:

**Input:**
root = [1]

makefile
Copy code

**Output:**
1

vbnet
Copy code

**Explanation:**
- The root node is always considered good.

## Approach

### 1. Problem Breakdown
- A "good" node is one where no node on the path from the root to this node has a value greater than this node's value.
- We need to traverse the tree, and for each node, check if its value is the maximum along the path from the root to that node.
- The traversal can be done using Depth First Search (DFS) or Breadth First Search (BFS).

### 2. Traversal Approach
- Use a recursive DFS function that passes along the maximum value encountered so far on the path from the root to the current node.
- If the current node's value is greater than or equal to the maximum value in the path, it is considered "good."
- The recursive function should visit both left and right children, keeping track of the maximum value for the current path.

### 3. Solution Steps:
1. Start at the root node and set the maximum value to the root's value.
2. Traverse down to each node, updating the maximum value along the path.
3. If the current node's value is greater than or equal to the current maximum, increase the count of good nodes.
4. Return the total count of good nodes after the traversal is complete.

## Constraints
- The number of nodes in the binary tree is in the range `[1, 10^5]`.
- Each node's value is between `[-10^4, 10^4]`.

## Time Complexity
- **Time Complexity:** `O(N)`, where `N` is the number of nodes in the binary tree. This is because we visit each node exactly once during the traversal.
- **Space Complexity:** `O(H)`, where `H` is the height of the tree. This accounts for the recursion stack in case of DFS.
