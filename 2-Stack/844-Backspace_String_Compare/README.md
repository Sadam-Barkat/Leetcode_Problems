# Problem: Backspace String Compare

## Description

Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. The `#` character means a backspace.

**Note:** After backspacing an empty text, the text will continue empty.

## Examples

### Example 1:
- **Input:** `s = "ab#c"`, `t = "ad#c"`
- **Output:** `true`
- **Explanation:** Both `s` and `t` become `"ac"`.

### Example 2:
- **Input:** `s = "ab##"`, `t = "c#d#"`
- **Output:** `true`
- **Explanation:** Both `s` and `t` become `""`.

### Example 3:
- **Input:** `s = "a#c"`, `t = "b"`
- **Output:** `false`
- **Explanation:** `s` becomes `"c"` while `t` becomes `"b"`.

## Constraints

- `1 <= s.length, t.length <= 200`
<<<<<<< HEAD
- `s` and `t` only contain lowercase letters and `#` characters
=======
- `s` and `t` only contain lowercase letters and `#` characters.
>>>>>>> b89779cf6f400de0112ab3ee025a93cf9be9b717
