# Minimize String Length After Removing Substrings

This problem involves reducing a given string by removing specific substrings iteratively until the minimum possible length is achieved. The task is to determine the smallest length of the resulting string.

## Problem Description

You are given a string `s` consisting only of uppercase English letters. You can perform operations where each operation involves removing any occurrence of the substrings "AB" or "CD" from `s`. After removing a substring, the remaining parts of `s` are concatenated, which could form new occurrences of "AB" or "CD" that can be removed in subsequent operations.

Your goal is to return the minimum possible length of the string after performing these operations as many times as possible.

### Examples

#### Example 1

**Input:**
```plaintext
s = "ABFCACDB"
Output:

plaintext
Copy code
2
Explanation:

We can perform the following operations:
Remove "AB" from "ABFCACDB", resulting in "FCACDB".
Remove "CD" from "FCACDB", resulting in "FCAB".
Remove "AB" from "FCAB", resulting in "FC".
The resulting length of the string is 2, which is the minimum possible.
Example 2
Input:

plaintext
Copy code
s = "ACBBD"
Output:

plaintext
Copy code
5
Explanation:

No occurrences of "AB" or "CD" can be removed from "ACBBD", so the length remains the same.
Constraints
1 <= s.length <= 100
s consists only of uppercase English letters.