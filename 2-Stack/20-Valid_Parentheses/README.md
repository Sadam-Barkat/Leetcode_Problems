# Valid Parentheses

## Problem Description

Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[`, and `]`, determine if the input string is valid. A string is considered valid if:

1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding open bracket of the same type.

## Examples

### Example 1
**Input:**  
`s = "()"`

**Output:**  
`true`

### Example 2
**Input:**  
`s = "()[]{}"`

**Output:**  
`true`

### Example 3
**Input:**  
`s = "(]"`

**Output:**  
`false`

### Example 4
**Input:**  
`s = "([])"`

**Output:**  
`true`

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists only of the characters `()[]{}`.

## Approach

1. **Use a Stack**: Traverse each character in `s`.
2. **Push Open Brackets**: For any opening bracket (`(`, `{`, `[`), push it onto the stack.
3. **Match Close Brackets**: For each closing bracket (`)`, `}`, `]`), check if it matches the top element of the stack:
   - If it matches, pop the stack.
   - If it doesn’t match or the stack is empty, return `false`.
4. **Final Check**: After processing all characters, if the stack is empty, the string is valid. Otherwise, it’s invalid.

This approach ensures that each open bracket has a correctly ordered and matching closing bracket, resulting in an efficient solution for validating parentheses.
