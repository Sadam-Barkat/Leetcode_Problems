# Minimum Add to Make Parentheses Valid

## Problem Description
A parentheses string is valid if and only if:
1. It is an empty string, or
2. It can be written as `AB` (A concatenated with B), where A and B are valid strings, or
3. It can be written as `(A)`, where A is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

For example:
- If `s = "()))"`, you can insert an opening parenthesis to make it `"(()))"` or a closing parenthesis to make it `"()))))"`.

**Goal:** Return the minimum number of moves required to make `s` valid.

---

## Examples

### Example 1
**Input:**  
`s = "())"`

**Output:**  
`1`

**Explanation:**  
We can insert one `(` to make the string valid: `"(())"`.

---

### Example 2
**Input:**  
`s = "((("`

**Output:**  
`3`

**Explanation:**  
We need three `)` to make the string valid: `"((()))"`.

---

## Constraints
- `1 <= s.length <= 1000`
- `s[i]` is either `'('` or `')'`.