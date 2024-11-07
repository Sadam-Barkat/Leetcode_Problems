# Baseball Game Score Calculation

## Problem Overview

In this problem, you are tasked with keeping track of the scores for a baseball game using a list of operations. Each operation either records a new score, calculates a score based on the previous scores, or invalidates the last recorded score.

## Operations

You will be given a list of operations where each operation is one of the following:

- **Integer x**: Record a new score of `x`.
- **'+'**: Record a new score that is the sum of the previous two scores.
- **'D'**: Record a new score that is double the previous score.
- **'C'**: Invalidate the previous score, removing it from the record.

## Objective

After processing all the operations, return the sum of all the scores recorded.

## Examples

### Example 1:

**Input**: `ops = ["5", "2", "C", "D", "+"]`

**Output**: `30`

**Explanation**:
- "5" → Record 5, record is now `[5]`.
- "2" → Record 2, record is now `[5, 2]`.
- "C" → Invalidate last score, record is now `[5]`.
- "D" → Double of 5, record is now `[5, 10]`.
- "+" → Sum of last two scores (5 + 10), record is now `[5, 10, 15]`.
- Total sum is `5 + 10 + 15 = 30`.

### Example 2:

**Input**: `ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]`

**Output**: `27`

**Explanation**:
- "5" → Record 5, record is now `[5]`.
- "-2" → Record -2, record is now `[5, -2]`.
- "4" → Record 4, record is now `[5, -2, 4]`.
- "C" → Invalidate last score, record is now `[5, -2]`.
- "D" → Double of -2, record is now `[5, -2, -4]`.
- "9" → Record 9, record is now `[5, -2, -4, 9]`.
- "+" → Sum of last two scores (-4 + 9), record is now `[5, -2, -4, 9, 5]`.
- "+" → Sum of last two scores (9 + 5), record is now `[5, -2, -4, 9, 5, 14]`.
- Total sum is `5 + -2 + -4 + 9 + 5 + 14 = 27`.

### Example 3:

**Input**: `ops = ["1", "C"]`

**Output**: `0`

**Explanation**:
- "1" → Record 1, record is now `[1]`.
- "C" → Invalidate last score, record is now `[]`.
- Total sum is `0`.

## Constraints

- `1 <= operations.length <= 1000`
- Each operation is either "C", "D", "+", or an integer within the range `[-3 * 10^4, 3 * 10^4]`.
- For operation "+", there will always be at least two previous scores on the record.
- For operations "C" and "D", there will always be at least one previous score on the record.

## Approach

You can iterate through the list of operations, maintaining a record of scores in a stack-like structure. Apply each operation to modify this list accordingly, and at the end, return the sum of the scores in the list.

## Conclusion

This problem requires you to simulate a sequence of operations on a list while maintaining the integrity of the scores. By using a stack-like approach, you can efficiently handle the operations and compute the final sum.
