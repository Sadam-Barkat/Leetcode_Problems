# Decode String

## Problem Statement
Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that:
- The input string is always valid (no extra white spaces, well-formed square brackets, etc.).
- The original data does not contain any digits; digits are only used for repeat numbers `k`. For example, there will not be inputs like `3a` or `2[4]`.

The test cases are generated so that the length of the output will never exceed `10^5`.

---

## Examples

### Example 1
**Input:**  
`s = "3[a]2[bc]"`  
**Output:**  
`"aaabcbc"`

### Example 2
**Input:**  
`s = "3[a2[c]]"`  
**Output:**  
`"accaccacc"`

### Example 3
**Input:**  
`s = "2[abc]3[cd]ef"`  
**Output:**  
`"abcabccdcdcdef"`

---

## Constraints
- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets `'[]'`.
- `s` is guaranteed to be a valid input.
- All integers in `s` are in the range `[1, 300]`.
