# Count Subarrays with Product Less Than K

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

### Example 1
- **Input**: `nums = [10, 5, 2, 6]`, `k = 100`
- **Output**: `8`
- **Explanation**: The 8 subarrays that have product less than 100 are:
  - `[10]`, `[5]`, `[2]`, `[6]`, `[10, 5]`, `[5, 2]`, `[2, 6]`, `[5, 2, 6]`
  - Note: `[10, 5, 2]` is not included as the product (100) is not strictly less than `k`.

### Example 2
- **Input**: `nums = [1, 2, 3]`, `k = 0`
- **Output**: `0`

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 10^6`

## Approach
To solve this problem efficiently:
- Use a **sliding window (two-pointer)** approach to keep track of the product of subarrays.
- Expand the right pointer to include more elements while keeping the product less than `k`.
- If the product becomes `>= k`, shrink the window from the left until the product is less than `k`.

