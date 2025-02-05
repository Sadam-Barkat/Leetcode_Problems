# Problem: Check if One String Swap Can Make Strings Equal

## Problem Description

You are given two strings `s1` and `s2` of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return `true` if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return `false`.

### Example 1:
**Input**: `s1 = "bank"`, `s2 = "kanb"`
**Output**: `true`
**Explanation**: For example, swap the first character with the last character of `s2` to make `"bank"`.

### Example 2:
**Input**: `s1 = "attack"`, `s2 = "defend"`
**Output**: `false`
**Explanation**: It is impossible to make them equal with one string swap.

### Example 3:
**Input**: `s1 = "kelb"`, `s2 = "kelb"`
**Output**: `true`
**Explanation**: The two strings are already equal, so no string swap operation is required.

## Constraints:
- The strings `s1` and `s2` are of the same length and have at least 1 character.
- The input strings are guaranteed to be non-empty.

## Approach

1. **Base Case**: If the strings are already equal, no swap is needed.
2. **Identify Differences**: Check the characters in the two strings to find where they differ.
3. **Check Swap Feasibility**: If exactly two characters differ, check if swapping them in one string can make the strings equal.
4. **Return the Result**: Return `True` if a valid swap is possible, otherwise return `False`.

## Complexity Analysis

- **Time Complexity**: O(n), where `n` is the length of the strings, as we only need to iterate through them once.
- **Space Complexity**: O(1), since we only use a constant amount of extra space for storing the indices of differences.

## Solution Code

You can find the solution code in the main program file.
