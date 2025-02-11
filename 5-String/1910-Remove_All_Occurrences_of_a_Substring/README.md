# Remove All Occurrences of a Substring

## Problem Statement
Given two strings `s` and `part`, perform the following operation on `s` until all occurrences of the substring `part` are removed:

1. Find the **leftmost occurrence** of the substring `part` in `s`.
2. Remove that occurrence from `s`.
3. Repeat the process until `part` no longer exists in `s`.
4. Return the modified string.

A **substring** is a contiguous sequence of characters in a string.

## Examples

### Example 1:
**Input:**
s = "daabcbaabcbc" part = "abc"

makefile
Copy
Edit
**Output:**
"dab"

markdown
Copy
Edit
**Explanation:**
1. `"daabcbaabcbc"` → Remove `"abc"` at index 2 → `"dabaabcbc"`
2. `"dabaabcbc"` → Remove `"abc"` at index 4 → `"dababc"`
3. `"dababc"` → Remove `"abc"` at index 3 → `"dab"`

### Example 2:
**Input:**
s = "axxxxyyyyb" part = "xy"

makefile
Copy
Edit
**Output:**
"ab"

markdown
Copy
Edit
**Explanation:**
1. `"axxxxyyyyb"` → Remove `"xy"` at index 4 → `"axxxyyyb"`
2. `"axxxyyyb"` → Remove `"xy"` at index 3 → `"axxyyb"`
3. `"axxyyb"` → Remove `"xy"` at index 2 → `"axyb"`
4. `"axyb"` → Remove `"xy"` at index 1 → `"ab"`

## Constraints
- `1 <= s.length <= 1000`
- `1 <= part.length <= 1000`
- `s` and `part` consist of lowercase English letters.
