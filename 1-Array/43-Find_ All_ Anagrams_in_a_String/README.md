# Find All Anagrams in a String

## Problem Description

Given two strings `s` and `p`, the task is to find all the starting indices of `p`'s **anagrams** in `s`. You can return the results in any order.

An **anagram** of a string is a rearrangement of the characters in that string.

### Examples

#### Example 1:
- **Input:** `s = "cbaebabacd"`, `p = "abc"`
- **Output:** `[0,6]`
- **Explanation:** 
  - The substring with start index `0` is `"cba"`, which is an anagram of `"abc"`.
  - The substring with start index `6` is `"bac"`, which is an anagram of `"abc"`.

#### Example 2:
- **Input:** `s = "abab"`, `p = "ab"`
- **Output:** `[0,1,2]`
- **Explanation:** 
  - The substring with start index `0` is `"ab"`, which is an anagram of `"ab"`.
  - The substring with start index `1` is `"ba"`, which is an anagram of `"ab"`.
  - The substring with start index `2` is `"ab"`, which is an anagram of `"ab"`.

### Constraints:
- `1 <= s.length, p.length <= 3 * 10^4`
- `s` and `p` consist of lowercase English letters only.

## Approach

1. **Sliding Window**: Since `p` and its anagrams are of the same length, we can use a fixed-length sliding window to iterate over `s`.
2. **Frequency Count**: Calculate the character frequency count of `p`, and for each window in `s`, check if it matches `p`'s frequency count.
3. **Optimized Comparison**: Instead of recalculating frequencies for every window, maintain a dynamic frequency count and update it as the window slides across `s`.

This approach ensures the solution is efficient and can handle large strings.


