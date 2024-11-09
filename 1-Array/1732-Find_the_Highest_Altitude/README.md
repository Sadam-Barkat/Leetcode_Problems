# Biker's Highest Altitude

## Problem Description
A biker is going on a road trip that consists of multiple points with different altitudes. The biker starts at **Point 0** with an altitude of `0`.

You are given an integer array `gain` of length `n`, where `gain[i]` represents the net gain or loss in altitude between **points i** and **i + 1**.

Your task is to calculate and return the **highest altitude** reached during the trip.

## Example

### Example 1
- **Input:** `gain = [-5, 1, 5, 0, -7]`
- **Output:** `1`
- **Explanation:** The altitudes at each point are:
  - Point 0: 0
  - Point 1: 0 + (-5) = -5
  - Point 2: -5 + 1 = -4
  - Point 3: -4 + 5 = 1
  - Point 4: 1 + 0 = 1
  - Point 5: 1 + (-7) = -6
  - The highest altitude reached is **1**.

### Example 2
- **Input:** `gain = [-4, -3, -2, -1, 4, 3, 2]`
- **Output:** `0`
- **Explanation:** The altitudes at each point are:
  - Point 0: 0
  - Point 1: 0 + (-4) = -4
  - Point 2: -4 + (-3) = -7
  - Point 3: -7 + (-2) = -9
  - Point 4: -9 + (-1) = -10
  - Point 5: -10 + 4 = -6
  - Point 6: -6 + 3 = -3
  - Point 7: -3 + 2 = -1
  - The highest altitude reached is **0**.

## Constraints
- `n == gain.length`
- `1 <= n <= 100`
- `-100 <= gain[i] <= 100`

## Approach
1. Start at an initial altitude of `0`.
2. Traverse through the `gain` array and calculate the altitude at each point by adding `gain[i]` to the previous altitude.
3. Track the highest altitude reached during the trip.
4. Return the highest altitude.

## Solution
This approach ensures that we calculate the altitude at each point and efficiently determine the maximum altitude in one pass through the array.
