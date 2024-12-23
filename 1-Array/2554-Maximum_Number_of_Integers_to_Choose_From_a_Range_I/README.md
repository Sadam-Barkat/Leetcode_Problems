# Maximum Number of Integers You Can Choose

## Problem Description

You are given an integer array `banned`, and two integers `n` and `maxSum`. The task is to choose some number of integers following these rules:

1. The chosen integers have to be in the range `[1, n]`.
2. Each integer can be chosen at most once.
3. The chosen integers should not be in the array `banned`.
4. The sum of the chosen integers should not exceed `maxSum`.

You need to return the maximum number of integers you can choose while following the mentioned rules.

## Example 1:

**Input:**

```python
banned = [1, 6, 5]
n = 5
maxSum = 6
Output:

python
Copy code
2
Explanation:

You can choose the integers 2 and 4.

Both 2 and 4 are from the range [1, 5], and neither appear in the banned array.
Their sum is 6, which does not exceed maxSum.
Example 2:
Input:

python
Copy code
banned = [1, 2, 3, 4, 5, 6, 7]
n = 8
maxSum = 1
Output:

python
Copy code
0
Explanation:

You cannot choose any integer from the range [1, 8] while following the conditions.

Example 3:
Input:

python
Copy code
banned = [11]
n = 7
maxSum = 50
Output:

python
Copy code
7
Explanation:

You can choose the integers 1, 2, 3, 4, 5, 6, 7. These integers are from the range [1, 7], all are not in the banned array, and their sum is 28, which does not exceed maxSum.

Constraints
1 <= banned.length <= 10^4
1 <= banned[i], n <= 10^4
1 <= maxSum <= 10^9