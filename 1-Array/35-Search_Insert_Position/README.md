## 35. Search Insert Position

### Problem Statement:
Given a sorted array of distinct integers `nums` and a target value `target`, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

### Example:
#### Input:
nums = [1, 3, 5, 6] target = 5

shell
Copy code
#### Output:
2

shell
Copy code

#### Input:
nums = [1, 3, 5, 6] target = 2

shell
Copy code
#### Output:
1

shell
Copy code

#### Input:
nums = [1, 3, 5, 6] target = 7

shell
Copy code
#### Output:
4

shell
Copy code

#### Input:
nums = [1, 3, 5, 6] target = 0

shell
Copy code
#### Output:
0

markdown
Copy code

#### Constraints:
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains distinct values sorted in ascending order.
- `-10^4 <= target <= 10^4`