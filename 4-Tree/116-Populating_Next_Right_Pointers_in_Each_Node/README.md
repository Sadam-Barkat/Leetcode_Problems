# Populate Next Right Pointers in Each Node

## Problem Description

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree is defined as:

```cpp
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
};
```

Your task is to populate each `next` pointer to point to its next right node. If there is no next right node, the `next` pointer should be set to `NULL`. Initially, all `next` pointers are set to `NULL`.

### Example 1:

#### Input:
```plaintext
root = [1,2,3,4,5,6,7]
```

#### Output:
```plaintext
[1,#,2,3,#,4,5,6,7,#]
```

#### Explanation:
Given the perfect binary tree:

```
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

The function should populate the `next` pointers to connect nodes at the same level:

```
        1 -> NULL
      /   \
     2  -> 3 -> NULL
    / \   / \
   4->5->6->7 -> NULL
```

The serialized output is in level order as connected by the `next` pointers, with `#` signifying the end of each level.

### Example 2:

#### Input:
```plaintext
root = []
```

#### Output:
```plaintext
[]
```

### Constraints:

- The number of nodes in the tree is in the range `[0, 2^{12} - 1]`.
- `-1000 <= Node.val <= 1000`.
