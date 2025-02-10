# Clear Digits from String

## Problem Statement
You are given a string `s` consisting of lowercase English letters and digits.  
Your task is to remove all digits by performing the following operation repeatedly:

- Delete the first digit found and the closest non-digit character to its left.

Return the resulting string after all digits are removed.

## Example Cases

### Example 1:
**Input:**  
```python
s = "abc"
Output:

python
Copy
Edit
"abc"
Explanation:
There are no digits in the string, so no changes are needed.

Example 2:
Input:

python
Copy
Edit
s = "cb34"
Output:

python
Copy
Edit
""
Explanation:

Remove 3 and closest non-digit b, string becomes "c4".
Remove 4 and closest non-digit c, string becomes "".
Solution Approach
The solution uses a stack-based approach:

Iterate through each character in the string.
If the character is a digit, remove the most recent non-digit character.
If the character is a letter, store it in a stack.
Finally, return the remaining characters as a string.s