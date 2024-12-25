# 2891. Method Chaining

## Problem Statement

You are given a DataFrame `animals` with the following columns:

| Column Name | Type   |
|-------------|--------|
| name        | object |
| species     | object |
| age         | int    |
| weight      | int    |

Write a solution to list the names of animals that weigh strictly more than 100 kilograms.

Return the animals sorted by weight in descending order.

### Example 1:

**Input:**
DataFrame `animals`:

| name     | species | age | weight |
|----------|---------|-----|--------|
| Tatiana  | Snake   | 98  | 464    |
| Khaled   | Giraffe | 50  | 41     |
| Alex     | Leopard | 6   | 328    |
| Jonathan | Monkey  | 45  | 463    |
| Stefan   | Bear    | 100 | 50     |
| Tommy    | Panda   | 26  | 349    |

**Output:**

| name     |
|----------|
| Tatiana  |
| Jonathan |
| Tommy    |
| Alex     |

**Explanation:**

All animals weighing more than 100 kilograms should be included in the results table. Tatiana's weight is 464, Jonathan's weight is 463, Tommy's weight is 349, and Alex's weight is 328. The results should be sorted in descending order of weight.

### Constraints:
- The DataFrame has at least one row.
- The weight of an animal is a non-negative integer.

### Notes:
- Method chaining in Pandas allows you to perform multiple operations in a single line, making the code more concise and readable.
