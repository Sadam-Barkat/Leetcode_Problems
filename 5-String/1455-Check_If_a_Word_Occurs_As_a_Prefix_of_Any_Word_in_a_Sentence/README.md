# Prefix Search in Sentence

## Problem Description

Given a sentence that consists of some words separated by a single space, and a `searchWord`, you need to check if `searchWord` is a prefix of any word in the sentence.

Return the index (1-indexed) of the word in the sentence where `searchWord` is a prefix of this word. If `searchWord` is a prefix of more than one word, return the index of the first word (minimal index). If there is no such word, return `-1`.

### Definition of a Prefix
A prefix of a string `s` is any leading contiguous substring of `s`.

## Example

### Example 1:
**Input:**
```python
sentence = "i love eating burger"
searchWord = "burg"


Constraints:
1 <= sentence.length <= 100
1 <= searchWord.length <= 10
sentence consists of lowercase English letters and spaces.
searchWord consists of lowercase English letters.