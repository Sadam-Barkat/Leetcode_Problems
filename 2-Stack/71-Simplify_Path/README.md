# Unix-Style File System Path Simplification

This problem involves simplifying an absolute Unix-style file path by following specific rules to derive the canonical path.

## Problem Description

Given an absolute file path for a Unix-style file system, transform it into its simplified canonical path. The rules for a Unix-style file system are as follows:

1. **Current Directory (".")**: A single period (`.`) represents the current directory and does not change the path.
2. **Parent Directory ("..")**: A double period (`..`) represents moving up one directory to the parent directory.
3. **Consecutive Slashes**: Multiple consecutive slashes (`//`, `///`, etc.) are treated as a single slash (`/`).
4. **Valid Names**: Any sequence of periods that doesn’t match `.` or `..` is treated as a valid directory or file name. For example, `...` and `....` are valid names.

The simplified canonical path should follow these rules:

- The path must start with a single slash (`/`).
- Directories must be separated by exactly one slash (`/`).
- The path must not end with a trailing slash unless it is the root directory.
- The path must not contain any `.` or `..` elements for current or parent directories.

Return the canonical form of the input path.

## Examples

### Example 1
**Input:**
```plaintext
path = "/home/"
Output:

plaintext
Copy code
"/home"
Explanation: The trailing slash is removed.

Example 2
Input:

plaintext
Copy code
path = "/home//foo/"
Output:

plaintext
Copy code
"/home/foo"
Explanation: Multiple consecutive slashes are replaced by a single slash.

Example 3
Input:

plaintext
Copy code
path = "/home/user/Documents/../Pictures"
Output:

plaintext
Copy code
"/home/user/Pictures"
Explanation: A double period .. moves up to the parent directory.

Example 4
Input:

plaintext
Copy code
path = "/../"
Output:

plaintext
Copy code
"/"
Explanation: Going up from the root directory is not allowed, so it remains at /.

Example 5
Input:

plaintext
Copy code
path = "/.../a/../b/c/../d/./"
Output:

plaintext
Copy code
"/.../b/d"
Explanation: ... is treated as a valid directory name.

Constraints
1 <= path.length <= 3000
path consists of English letters, digits, periods (.), slashes (/), or underscores (_).
path is a valid absolute Unix path.