# Maximum Average Subarray I

## Problem Description

Given an integer array `nums` and an integer `k`, the task is to find a contiguous subarray of length `k` that has the maximum average value, and return this value. The answer can have a calculation error of less than \(10^{-5}\).

### Examples

#### Example 1:
- **Input:** `nums = [1,12,-5,-6,50,3]`, `k = 4`
- **Output:** `12.75000`
- **Explanation:** The subarray with the maximum average is `[12, -5, -6, 50]`, giving an average of `(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75`.

#### Example 2:
- **Input:** `nums = [5]`, `k = 1`
- **Output:** `5.00000`
- **Explanation:** Since there is only one element and `k = 1`, the average is simply the element itself, `5.0`.

### Constraints:
- `n == nums.length`
- `1 <= k <= n <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Approach

1. **Sliding Window Technique**: To find the subarray with the maximum average, use a sliding window of length `k`. 
2. **Initial Sum Calculation**: Calculate the sum of the first `k` elements.
3. **Window Slide**: Slide the window across `nums` by adding the next element and removing the previous element in each step.
4. **Track Maximum Sum**: Track the maximum sum encountered and calculate the average based on it.

This approach is efficient with a linear time complexity.


