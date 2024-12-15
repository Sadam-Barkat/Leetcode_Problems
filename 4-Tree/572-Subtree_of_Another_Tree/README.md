# Check if a Binary Tree is a Subtree of Another

## Problem Description

Given the roots of two binary trees, `root` and `subRoot`, determine whether `subRoot` is a subtree of `root`. A subtree of a binary tree is defined as a tree that consists of a node in the binary tree and all of its descendants. The binary tree itself is also considered a subtree of itself.

### Example 1:

**Input:**
```
root = [3,4,5,1,2], subRoot = [4,1,2]
```
**Output:**
```
true
```

### Example 2:

**Input:**
```
root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
```
**Output:**
```
false
```

### Constraints:
- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- `-10^4 <= root.val <= 10^4`
- `-10^4 <= subRoot.val <= 10^4`

## Key Points to Consider
1. **Structure Match:** The subtree must have the same structure and node values as the corresponding part of the main tree.
2. **Edge Cases:**
    - `subRoot` is `null`: Should always return `true` as an empty tree is a subtree of any tree.
    - `root` is `null` but `subRoot` is not: Should return `false`.
    - Both `root` and `subRoot` are identical: Should return `true`.

## Input Format
- `root`: The root node of the main binary tree.
- `subRoot`: The root node of the binary tree to check as a subtree.

## Output Format
- A boolean value:
  - `true`: If `subRoot` is a subtree of `root`.
  - `false`: Otherwise.

## Examples

### Example 1:
**Input:**
```
root = [3,4,5,1,2], subRoot = [4,1,2]
```
**Output:**
```
true
```
**Explanation:**
The subtree with root node `4` in the main tree matches the `subRoot`.

### Example 2:
**Input:**
```
root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
```
**Output:**
```
false
```
**Explanation:**
Although there is a node `4` in the main tree, its subtree does not match the structure and values of `subRoot`.

## Constraints
1. The values in the tree can be negative.
2. Both trees can have up to 2000 nodes, making efficiency an important consideration.

---

### How to Use This Repository
This repository provides a solution to the problem of checking if a tree is a subtree of another. Clone this repository and follow the instructions in the respective files to understand and implement the solution.
