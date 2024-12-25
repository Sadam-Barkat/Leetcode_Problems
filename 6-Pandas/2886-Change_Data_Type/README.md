# 2886. Change Data Type

## Problem Statement

You are given a **0-indexed** array `data` containing strings, where each string represents a data value. Additionally, you are provided with a target data type `targetType`. Your task is to convert each element in `data` to the specified `targetType` and return the resulting array.

### Conversion Rules:
- If `targetType` is `"int"`, convert each string to an integer.
- If `targetType` is `"float"`, convert each string to a floating-point number.
- If `targetType` is `"str"`, keep each string as is.

If any conversion is invalid (e.g., converting a non-numeric string to `"int"` or `"float"`), replace the value with `null` (or `None` in Python).

### Example 1:
Input: data = ["1", "2", "3.5", "four"], targetType = "int"  
Output: [1, 2, null, null]  

Explanation:  
- "1" and "2" are valid integers.  
- "3.5" and "four" cannot be converted to integers, so they are replaced with `null`.

### Example 2:
Input: data = ["1.1", "2.2", "three", "4.0"], targetType = "float"  
Output: [1.1, 2.2, null, 4.0]  

Explanation:  
- "1.1", "2.2", and "4.0" are valid floating-point numbers.  
- "three" cannot be converted to a float, so it is replaced with `null`.

### Constraints:
- `1 <= data.length <= 1000`
- `1 <= data[i].length <= 10`
- `targetType` is one of `"int"`, `"float"`, or `"str"`.
