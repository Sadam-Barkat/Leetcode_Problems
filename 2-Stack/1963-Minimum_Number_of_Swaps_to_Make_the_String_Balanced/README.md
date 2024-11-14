# Minimum Swaps to Balance a Bracket String

## Problem Description

You are given a 0-indexed string `s` of even length `n`, consisting of exactly `n / 2` opening brackets `'['` and `n / 2` closing brackets `']'`. A string is considered balanced if:
- It is empty.
- It can be written as `AB`, where both `A` and `B` are balanced strings.
- It can be written as `[C]`, where `C` is a balanced string.

The task is to determine the minimum number of swaps needed to make the string `s` balanced. In each swap, any two brackets at different indices can be exchanged.

### Examples

#### Example 1
**Input:**  
`s = "][]["`  
**Output:**  
`1`  
**Explanation:**  
Swapping the brackets at indices 0 and 3 results in the balanced string `"[[]]"`.

#### Example 2
**Input:**  
`s = "]]][[["`  
**Output:**  
`2`  
**Explanation:**  
The following swaps balance the string:
1. Swap index 0 with index 4 to get `"[]][]["`.
2. Swap index 1 with index 5 to get `"[[][]]"`.

#### Example 3
**Input:**  
`s = "[]"`  
**Output:**  
`0`  
**Explanation:**  
The string is already balanced.

### Constraints

- `n == s.length`
- `2 <= n <= 10^6`
- `n` is even.
- `s[i]` is either `'['` or `']'`.
- The number of opening brackets `'['` is equal to the number of closing brackets `']'`.

## Solution Approach

We solve this problem by using a stack to track unbalanced brackets:

1. Iterate through each character in the string `s`.
2. For each opening bracket `'['`, add it to the stack.
3. For each closing bracket `']'`, if there is an unmatched opening bracket in the stack, pop it to mark it as balanced.
4. If there is no unmatched opening bracket available, increment a counter (`unbalanced_closing`) to track unbalanced closing brackets.
5. The minimum number of swaps required is half of the `unbalanced_closing` value since each swap fixes one unbalanced pair.

This approach ensures an efficient solution even for large values of `n`.

