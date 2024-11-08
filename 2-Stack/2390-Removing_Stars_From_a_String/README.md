# Remove Characters with Stars

## Problem Description

Given a string `s` containing lowercase English letters and stars (`*`), perform the following operation for each star:

1. Choose a star `*` in `s`.
2. Remove the closest non-star character to its left and the star itself.

Repeat this until all stars are processed. The input guarantees that the operations are always possible, and the resulting string will always be unique.

## Examples

### Example 1
**Input:**  
`s = "leet**cod*e"`

**Output:**  
`"lecoe"`

**Explanation:**  
- Remove the closest non-star character to the left of the first `*`: `"t"` in `"leet**cod*e"`, resulting in `"lee*cod*e"`.
- Repeat for the next `*`: Remove `"e"` from `"lee*cod*e"`, resulting in `"lecod*e"`.
- For the next `*`, remove `"d"` from `"lecod*e"`, resulting in `"lecoe"`.

### Example 2
**Input:**  
`s = "erase*****"`

**Output:**  
`""`

**Explanation:**  
All characters are removed by the stars, so the output is an empty string.

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters and stars `*`.

## Approach

1. Use a stack to build the resulting string by processing each character in `s`.
2. If the character is a non-star letter, push it onto the stack.
3. If the character is a `*`, pop the last element from the stack (the closest non-star character).
4. Continue until all characters in `s` are processed.
5. The stack will contain the resulting string after all operations.

