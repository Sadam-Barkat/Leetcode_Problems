class Solution:
    def maxWidthRamp(self, nums)-> int:
        res = 0
        n = len(nums)

        list1 = [(nums[i], i) for i in range(n)]

        list1.sort()

        min_index = list1[0][1]

        for i in range(1, n):
            current_index = list1[i][1]
            res = max(res, current_index - min_index)
            min_index = min(min_index, current_index)

        return res   