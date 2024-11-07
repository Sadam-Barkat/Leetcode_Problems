# Make Good String

## Problem Description
Given a string `s` of mixed lower and upper case English letters, a **good** string is defined as a string that does not have two adjacent characters `s[i]` and `s[i + 1]` where:
- `s[i]` is a lower-case letter, and `s[i + 1]` is the same letter but in upper-case (or vice versa).

To make a string "good," you can remove any two adjacent characters that make it "bad." This process continues until no adjacent bad pairs remain in the string.

Return the resulting string after making it "good." If the string is already good, it remains unchanged. If it becomes empty, return an empty string. The answer is guaranteed to be unique under the given constraints.

## Examples

### Example 1
- **Input:** `s = "leEeetcode"`
- **Output:** `"leetcode"`
- **Explanation:** Removing either `"Ee"` at index 1 or index 2 results in `"leetcode"`.

### Example 2
- **Input:** `s = "abBAcC"`
- **Output:** `""`
- **Explanation:** Removing all adjacent pairs like `"bB"`, `"aA"`, and `"cC"` makes the string empty.

### Example 3
- **Input:** `s = "s"`
- **Output:** `"s"`
- **Explanation:** Since there are no bad pairs, the output remains the same.

## Constraints
- `1 <= s.length <= 100`
- `s` contains only lower and upper case English letters.

## Approach
1. Use a stack data structure to process each character in the string.
2. For each character:
   - If the stack is not empty, and the top of the stack is the same letter as the current character but in the opposite case, remove (pop) the top element.
   - Otherwise, push the current character onto the stack.
3. After processing all characters, join the stack into a string, which is the "good" string.

## Complexity
- **Time Complexity:** O(n), where `n` is the length of the string. We iterate over each character once.
- **Space Complexity:** O(n) for the stack used to store characters that do not cancel out.

## Edge Cases
1. **Empty String:** An empty string is trivially "good."
2. **Single Character:** A single character string is always "good."
3. **All Good Pairs:** Strings that alternate bad pairs will be reduced to an empty string.
4. **No Bad Pairs:** Strings without bad pairs remain unchanged.

