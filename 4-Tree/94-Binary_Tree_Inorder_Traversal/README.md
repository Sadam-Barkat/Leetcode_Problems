# Inorder Traversal of a Binary Tree

## Problem Statement

Given the root of a binary tree, return the inorder traversal of its nodes' values.

## Examples

### Example 1:
**Input:**  
`root = [1, null, 2, 3]`  

**Output:**  
`[1, 3, 2]`  

**Explanation:**  
The inorder traversal visits nodes in the order: Left → Root → Right.

---

### Example 2:
**Input:**  
`root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]`  

**Output:**  
`[4, 2, 6, 5, 7, 1, 3, 9, 8]`  

**Explanation:**  
The inorder traversal follows the Left → Root → Right pattern, recursively visiting each subtree.

---

### Example 3:
**Input:**  
`root = []`  

**Output:**  
`[]`  

**Explanation:**  
An empty tree has no nodes to traverse.

---

### Example 4:
**Input:**  
`root = [1]`  

**Output:**  
`[1]`  

**Explanation:**  
A single-node tree returns the value of the root.

---

## Constraints:
1. The number of nodes in the tree is in the range `[0, 100]`.
2. `-100 <= Node.val <= 100`
