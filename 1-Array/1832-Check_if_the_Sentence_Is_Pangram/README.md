# Pangram Checker

This problem asks to determine whether a given string is a pangram or not. A pangram is a sentence where every letter of the English alphabet appears at least once.

## Problem Description

You are given a string `sentence` containing only lowercase English letters. Your task is to return `true` if the sentence is a pangram, or `false` otherwise.

### Example 1

**Input:**
```python
sentence = "thequickbrownfoxjumpsoverthelazydog"
Output:

python
Copy code
True
Explanation: The sentence contains at least one occurrence of every letter in the English alphabet.

Example 2
Input:

python
Copy code
sentence = "leetcode"
Output:

python
Copy code
False
Explanation: The sentence does not contain all the letters of the English alphabet (it misses some letters).

Constraints
1 <= sentence.length <= 1000
sentence consists only of lowercase English letters.