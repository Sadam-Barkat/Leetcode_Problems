# Number Container System

## Problem Statement
Design a number container system that supports the following operations:

1. **Insert or Replace** a number at a given index.
2. **Find** the smallest index that contains a given number.

### **Implementation**
We implement the `NumberContainers` class with:
- `change(index, number)`: Updates the mapping of indices and numbers.
- `find(number)`: Returns the smallest index containing the given number or `-1` if it does not exist.

## **Solution Approach**
This solution uses:
- A dictionary (`index_to_number`) to track which number is assigned to an index.
- A dictionary (`number_to_indices`) to maintain a **sorted list** of indices for each number.
- **Binary search (`bisect` module)** for efficient insertion and removal, ensuring `O(log N)` operations.

## **Complexity Analysis**
| Operation       | Complexity |
|----------------|------------|
| `change()`     | O(log N)   |
| `find()`       | O(1)       |


           
