# Number of Distinct Colors Among the Balls

## Problem Statement

```python
# You are given an integer `limit` and a `2D` array `queries` of size `n x 2`.
# There are `limit + 1` balls with distinct labels in the range `[0, limit]`.
# Initially, all balls are uncolored.
# For each query `[x, y]`, you mark ball `x` with the color `y`.
# After each query, find the number of distinct colors among the balls.
# Return an array `result` of length `n`, where `result[i]` denotes the number of distinct colors after the `i-th` query.
Example 1
python
Copy
Edit
limit = 4
queries = [[1, 4], [2, 5], [1, 3], [3, 4]]

# Output:
[1, 2, 2, 3]
Example 2
python
Copy
Edit
limit = 4
queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]

# Output:
[1, 2, 2, 3, 4]
Constraints
python
Copy
Edit
1 <= limit <= 10**9
1 <= n == queries.length <= 10**5
queries[i].length == 2
0 <= queries[i][0] <= limit
1 <= queries[i][1] <= 10**9